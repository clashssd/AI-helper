"""AI-helper/ai_engine/orchestrator/orchestrator.py"""
import asyncio
import json
import logging
import os
import shutil
from typing import Any, Dict
from PIL import Image
try:
    import pytesseract
except ImportError:
    pytesseract = None

try:
    from gatesolve_selenium import solve_on_page  # type: ignore
except ImportError:
    solve_on_page = None
from ai_engine.LLMclient import AIClient
from .models import Session, Task, AgentState
from .agent_factory import AgentFactory
from .session_manager import SessionManager
from browser_engine.BrowserOpen import run_selenium_engine, close_selenium_engine
from browser_engine.profile_creator.BuilderProfile import BuilderProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)

def setup_tesseract():
    if not pytesseract:
        return False
    if shutil.which("tesseract"):
        return True
    possible_paths = [
        r'C:\Program Files\Tesseract-OCR\tesseract.exe',
        r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe',
        os.path.expanduser(r'~\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'),
    ]
    for path in possible_paths:
        if os.path.exists(path):
            pytesseract.pytesseract.tesseract_cmd = path
            return True
    logger.error("Tesseract not found!")
    return False

TESSERACT_READY = setup_tesseract()


class Orchestrator:
    def __init__(self, ai_client: AIClient, max_workers: int = 1):
        self.ai = ai_client
        self.session_manager = SessionManager()
        self.max_workers = max_workers
        self.active_drivers = {}
    def _execute_tool(self, session_id: str, tool_name: str, args: dict) -> str:
        logger.info(f"[{session_id}] executing tool: {tool_name} with args: {args}")
        driver = self.active_drivers.get(session_id)

        if tool_name == "open_browser":
            url = args.get("url")
            if not url:
                return "Error: URL is required."
            if driver:
                logger.info(f"[{session_id}] Browser is already open. Current URL: {driver.current_url}")
                return f"Browser is already open. Current URL is {driver.current_url}. DO NOT call open_browser again."
            profile = BuilderProfile.build_profile()
            driver = run_selenium_engine(url, profile=profile)
            if driver:
                self.active_drivers[session_id] = driver
                return f"Success: Browser opened at {url}. Page title: {driver.title}"
            return "Error: Failed to open browser."
        if not driver:
            return "Error: Browser is not open. Call 'open_browser' first."
        if tool_name == "get_page_source":
            return driver.page_source[:12000]
        elif tool_name == "type_text":
            selector, text = args.get("selector"), args.get("text")
            try:
                element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
                element.clear()
                element.send_keys(text)
                return f"Success: Typed '{text}' into '{selector}'."
            except Exception as e:
                return f"Error typing text: {e}"
        elif tool_name == "click_element":
            if not driver:
                return "Error: Browser is not open."
            selector = args.get("selector")
            try:
                if "next" in selector.lower() or "go back" in selector.lower() or "next" in args.get("text",
                                                                                                     "").lower():
                    xpath = "//button[contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'next') or contains(translate(., 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'go back')]"
                    logger.info(f"[{session_id}] Smart Click: Looking for Next/Go back button via XPath.")
                    element = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, xpath))
                    )
                    element.click()
                    return f"Success: Clicked Next/Go back button."
                element = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                )
                element.click()
                return f"Success: Clicked '{selector}'."
            except Exception as e:
                return f"Error clicking element: {e}"
        elif tool_name == "get_interactive_elements":
            js_script = """
                return Array.from(document.querySelectorAll('input, button, a, select, textarea, [role="combobox"], [role="listbox"]')).map(el => {
                    return {
                        tag: el.tagName, type: el.type || '', id: el.id || '', name: el.name || '',
                        placeholder: el.placeholder || '', role: el.getAttribute('role') || '',
                        ariaLabel: el.getAttribute('aria-label') || '', text: el.innerText ? el.innerText.substring(0, 30) : ''
                    };
                }).filter(el => el.type !== 'hidden'); 
            """
            try:
                elements = driver.execute_script(js_script)
                return json.dumps(elements, ensure_ascii=False, indent=2)
            except Exception as e:
                return f"Error getting interactive elements: {e}"
        elif tool_name == "solve_captcha":
            captcha_type = args.get("captcha_type", "image").lower()
            if captcha_type == "image" and TESSERACT_READY:
                try:
                    img_selector = args.get("selector")
                    captcha_img = driver.find_element(By.CSS_SELECTOR, img_selector) if img_selector else driver.find_element(By.XPATH, "//img[contains(@src, 'captcha') or contains(@id, 'captcha')]")
                    img_path = f"captcha_{session_id}.png"
                    captcha_img.screenshot(img_path)
                    result = pytesseract.image_to_string(Image.open(img_path), config='--psm 8').strip()
                    os.remove(img_path)
                    return f"Success: CAPTCHA recognized as '{result}'."
                except Exception as e:
                    return f"Error solving image CAPTCHA: {e}"
            elif captcha_type in ["recaptcha", "hcaptcha", "turnstile"] and solve_on_page:
                api_key = os.getenv("GATESOLVE_API_KEY")
                if not api_key: return "Error: GATESOLVE_API_KEY missing."
                try:
                    solve_on_page(driver, api_key=api_key)
                    return "Success: CAPTCHA solved."
                except Exception as e:
                    return f"Error solving CAPTCHA: {e}"
            return "Error: CAPTCHA type unsupported or tool missing."
        elif tool_name == "select_option":
            if not driver:
                return "Error: Browser is not open."
            selector = args.get("selector")
            text = args.get("text")
            try:
                import time
                from selenium.webdriver.common.action_chains import ActionChains
                from selenium.webdriver.common.keys import Keys

                logger.info(f"[{session_id}] Trying to select '{text}' from '{selector}'")

                # 1. Находим сам дропдаун
                try:
                    element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                    )
                except:
                    element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located(
                            (By.XPATH, f"//div[@role='combobox'][contains(., '{selector}')]"))
                    )
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
                time.sleep(0.5)
                driver.execute_script("arguments[0].click();", element)
                time.sleep(1.5)
                js_find_and_click = f"""
                        var items = Array.from(document.querySelectorAll('li[role="option"], div[role="option"], ul[role="listbox"] li'));
                        var target = items.find(el => el.innerText.trim().toLowerCase() === '{text.toLowerCase()}' || el.innerText.trim().toLowerCase().includes('{text.toLowerCase()}'));
                        if (target) {{
                            // Иногда Google требует кликнуть по вложенному span
                            var innerSpan = target.querySelector('span');
                            if (innerSpan) innerSpan.click();
                            else target.click();
                            return true;
                        }}
                        return false;
                    """
                clicked = driver.execute_script(js_find_and_click)
                if clicked:
                    time.sleep(1)
                    element.send_keys(Keys.ESCAPE)
                    return f"Success: Selected '{text}' from dropdown."
                logger.warning(f"[{session_id}] JS didn't find '{text}', using keyboard.")
                element.send_keys(Keys.ARROW_DOWN)
                element.send_keys(Keys.ENTER)
                time.sleep(1)
                return f"Warning: Used keyboard to select '{text}'."
            except Exception as e:
                return f"Error selecting option '{text}': {e}"
        elif tool_name == "close_browser":
            close_selenium_engine(driver)
            self.active_drivers.pop(session_id, None)
            return "Success: Browser closed."
        return f"Error: Tool {tool_name} not found."
    async def _run_agent(self, agent_name: str, agent_state: AgentState, task: str, session_id: str, history: list = None) -> str:
        logger.info(f"=== Agent [{agent_name}] started. Task: {task} ===")
        messages = history or []
        messages.append({"role": "user", "content": f"Your task: {task}"})
        max_steps = 15
        for step in range(max_steps):
            await asyncio.sleep(5.0)
            response = await asyncio.to_thread(
                self.ai.ask,
                system_prompt=agent_state.system_prompt,
                tools=agent_state.tools,
                messages=messages,
            )
            if not response:
                logger.error(f"[{agent_name}] AI returned empty response.")
                return "Error: AI stopped responding."
            resp_dict = {"role": "assistant", "content": response.content or ""}
            if response.tool_calls:
                resp_dict["tool_calls"] = [
                    {"id": tc.id, "type": "function", "function": {"name": tc.function.name, "arguments": tc.function.arguments}}
                    for tc in response.tool_calls
                ]
            messages.append(resp_dict)
            if not response.tool_calls:
                logger.info(f"[{agent_name}] Finished without tool calls.")
                return response.content or "Task completed."
            is_finished = False
            final_result = ""
            for tool_call in response.tool_calls:
                tool_name = tool_call.function.name
                args = json.loads(tool_call.function.arguments)
                if tool_name == "spawn_agent":
                    role = args.get("role")
                    child_task = args.get("task")
                    child_state = AgentFactory.get_agent_state(role)
                    child_result = await self._run_agent(
                        agent_name=role,
                        agent_state=child_state,
                        task=child_task,
                        session_id=session_id
                    )
                    current_url = "unknown"
                    if session_id in self.active_drivers:
                        current_url = self.active_drivers[session_id].current_url
                    result = f"Child agent '{role}' finished. Current URL: {current_url}. Result: {child_result}"
                elif tool_name == "agent_finish":
                    result = "Agent finished."
                    final_result = args.get("result", "")
                    is_finished = True
                else:
                    result = await asyncio.to_thread(self._execute_tool, session_id, tool_name, args)
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": tool_name,
                    "content": str(result),
                })
            if is_finished:
                logger.info(f"=== Agent [{agent_name}] finished. Result: {final_result} ===")
                return final_result
        return "Error: Max steps reached without finishing."
    def start_and_run_session(self, goal: str) -> str:
        logger.info(f"Starting Strix-like session for goal: {goal}")
        session = Session(main_goal=goal)
        self.session_manager.save_session(session)
        root_agent = AgentFactory.create_root_agent(goal)
        try:
            final_result = asyncio.run(self._run_agent(
                agent_name="RootOrchestrator",
                agent_state=root_agent,
                task=goal,
                session_id=session.session_id
            ))
        except KeyboardInterrupt:
            logger.warning("Interrupted by user.")
            final_result = "Interrupted"
        finally:
            for session_id, driver in self.active_drivers.items():
                try:
                    close_selenium_engine(driver)
                except Exception:
                    pass
            self.active_drivers.clear()
        session.status = "finished"
        if session.tasks:
            session.tasks[0].result = final_result
        self.session_manager.save_session(session)
        return final_result