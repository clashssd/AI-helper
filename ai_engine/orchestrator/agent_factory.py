"""AI-helper/ai_engine/orchestrator/agent_factory.py"""
from .models import AgentState

class AgentFactory:
    @staticmethod
    def _get_browser_tools():
        return [
            {
                "type": "function",
                "function": {
                    "name": "open_browser",
                    "description": "Opens an anti-detect browser at the specified URL.",
                    "parameters": {
                        "type": "object",
                        "properties": {"url": {"type": "string"}},
                        "required": ["url"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "get_interactive_elements",
                    "description": "Returns a JSON list of all interactive elements (inputs, buttons, dropdowns) on the current page.",
                    "parameters": {"type": "object", "properties": {}}
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "type_text",
                    "description": "Types text into an input field.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "selector": {"type": "string"},
                            "text": {"type": "string"}
                        },
                        "required": ["selector", "text"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "click_element",
                    "description": "Clicks on a button or link. You can pass text like 'Next' or 'Go back' to find buttons by text.",
                    "parameters": {
                        "type": "object",
                        "properties": {"selector": {"type": "string"}},
                        "required": ["selector"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "select_option",
                    "description": "Selects an option from a dropdown menu.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "selector": {"type": "string"},
                            "text": {"type": "string"}
                        },
                        "required": ["selector", "text"]
                    }
                }
            }
        ]

    @staticmethod
    def _get_captcha_tools():
        return [
            {
                "type": "function",
                "function": {
                    "name": "solve_captcha",
                    "description": "Solves a CAPTCHA on the current page.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "captcha_type": {"type": "string", "description": "'recaptcha', 'hcaptcha', 'turnstile', or 'image'"}
                        },
                        "required": ["captcha_type"]
                    }
                }
            }
        ]

    @staticmethod
    def _get_finish_tool():
        return {
            "type": "function",
            "function": {
                "name": "agent_finish",
                "description": "Call this when your task is complete to return the result to the orchestrator.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "result": {"type": "string", "description": "Report of what you accomplished"}
                    },
                    "required": ["result"]
                }
            }
        }

    @staticmethod
    def _get_orchestrator_tools():
        return [
            {
                "type": "function",
                "function": {
                    "name": "spawn_agent",
                    "description": "Spawns a specialized child agent to handle a specific sub-task.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "role": {
                                "type": "string",
                                "enum": ["FormFiller", "CaptchaSolver"], # Убрали BrowserNavigator
                                "description": "The role of the child agent."
                            },
                            "task": {"type": "string", "description": "Specific instructions for the child."}
                        },
                        "required": ["role", "task"]
                    }
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "agent_finish",
                    "description": "Call this when the OVERALL GOAL is complete.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "result": {"type": "string", "description": "Final report or extracted data"}
                        },
                        "required": ["result"]
                    }
                }
            }
        ]
    @staticmethod
    def create_root_agent(goal: str) -> AgentState:
        prompt = (
            f"You are the Root Orchestrator. Your goal is: {goal}\n"
            "You manage a team. You MUST use the 'FormFiller' agent to do the actual work (opening browser, typing, clicking).\n"
            "If a CAPTCHA appears, spawn 'CaptchaSolver'.\n"
            "Do not try to open the browser yourself. Spawn 'FormFiller' with clear instructions.\n"
            "Once the FormFiller reports success, call 'agent_finish' with the final report."
        )
        return AgentState(
            name="RootOrchestrator",
            system_prompt=prompt,
            tools=AgentFactory._get_orchestrator_tools()
        )
    @staticmethod
    def create_form_filler_agent() -> AgentState:
        prompt = (
            "You are an autonomous Web Automation Agent. Your job is to complete the UI test flow.\n"
            "CRITICAL RULES:\n"
            "1. If the browser is not open, use 'open_browser'.\n"
            "2. Use 'get_interactive_elements' to see the page.\n"
            "3. Use 'type_text' for text inputs and 'select_option' for dropdowns.\n"
            "4. Use 'click_element' to click buttons. If you need to click 'Next' or 'Go back', just pass that text as the selector (e.g., selector='Next').\n"
            "5. If you see a modal about privacy or age, click 'Go back' to close it.\n"
            "When you reach the final step, call 'agent_finish' with the credentials."
        )
        return AgentState(
            name="FormFiller",
            system_prompt=prompt,
            tools=AgentFactory._get_browser_tools() + [AgentFactory._get_finish_tool()]
        )
    @staticmethod
    def create_captcha_agent() -> AgentState:
        prompt = (
            "You are a QA Visual Blocker Handler. Your job is to use the 'solve_captcha' tool to bypass visual verification. "
            "Call 'agent_finish' when the obstruction is cleared."
        )
        return AgentState(
            name="CaptchaSolver",
            system_prompt=prompt,
            tools=AgentFactory._get_captcha_tools() + [AgentFactory._get_finish_tool()]
        )
    @staticmethod
    def get_agent_state(role: str) -> AgentState:
        if role == "FormFiller":
            return AgentFactory.create_form_filler_agent()
        elif role == "CaptchaSolver":
            return AgentFactory.create_captcha_agent()
        else:
            return AgentFactory.create_form_filler_agent()