"""AI-helper/profile_creator/OptionsBuilder.py"""
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from .ProfileSchema import ProfileSchema
#Logger conf
logger = logging.getLogger(__name__)

class OptionsBuilder:
    """Converts a ProfileSchema object into ChromeOptions + JS scripts"""
    @staticmethod
    def build_options(profile: ProfileSchema) -> Options:
        """Creates and configures a ChromeOptions object based on a profile."""
        logger.info(f"Building ChromeOptions for profile: {profile.profile_name}")
        options = Options()
        #Core arguments for concealing automation
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        #Setting the User-Agent
        if profile.user_agent:
            options.add_argument(f'--user-agent={profile.user_agent}')
        #Setting the language
        if profile.language:
            options.add_argument(f'--lang={profile.language.split(",")[0]}')
        #Setting the window size
        options.add_argument(f'--window-size={profile.screen_width},{profile.screen_height + 100}')
        #Setting Proxy
        if profile.proxy:
            options.add_argument(f'--proxy-server={profile.proxy}')
            logger.info(f"Proxy set: {profile.proxy}")
        if profile.user_data_dir:
            options.add_argument(f"--user-data-dir={profile.user_data_dir}")
        #Additional custom arguments (if provided)
        for arg in profile.custom_args:
            options.add_argument(arg)
        # Disable "pop-up" notifications about insecure connections, etc.
        options.add_argument("--ignore-certificate-errors")
        options.add_argument("--ignore-ssl-errors")
        return options
    @staticmethod
    def get_js_script(profile: ProfileSchema) -> str:
        """
        Returns a JS script for injection into the browser.
        This script overrides parameters that Selenium cannot modify via Options.
        """
        logger.info(f"Generating JS injection script for profile: {profile.profile_name}")
        #Forming string for script
        script = f"""
        Object.defineProperty(navigator, 'webdriver', {{get: () => undefined}});
        Object.defineProperty(navigator, 'hardwareConcurrency', {{get: () => {profile.hardware_concurrency}}});
        Object.defineProperty(navigator, 'deviceMemory', {{get: () => {profile.device_memory}}});
        Object.defineProperty(navigator, 'platform', {{get: () => '{profile.platform}'}});
        const getParameter = WebGLRenderingContext.prototype.getParameter;
        WebGLRenderingContext.prototype.getParameter = function(parameter) {{
            if (parameter === 37445) {{
                return '{profile.webgl_vendor}';
            }}
            if (parameter === 37446) {{
                return '{profile.webgl_renderer}';
            }}
            return getParameter.apply(this, arguments);
        }};
        """
        #For mobile
        if profile.os_type in ["Android", "iOS"]:
            script += """
            Object.defineProperty(navigator, 'maxTouchPoints', {get: () => 5});
            window.ontouchstart = null;
            """
        return script