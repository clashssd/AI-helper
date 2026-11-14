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
        #Add canvas noise  script to JS
        script += """
                const originalGetImageData = CanvasRenderingContext2D.prototype.getImageData;
                CanvasRenderingContext2D.prototype.getImageData = function(x, y, w, h) {
                    const imageData = originalGetImageData.apply(this, arguments);
                    if (imageData.data.length > 0) {
                        // Вносим случайный шум в красный канал первого пикселя
                        imageData.data[0] = imageData.data[0] ^ 1; 
                    }
                    return imageData;
                };
                """
        # Add audio noise script to JS
        script += """
                const originalGetChannelData = AudioBuffer.prototype.getChannelData;
                AudioBuffer.prototype.getChannelData = function() {
                    const data = originalGetChannelData.apply(this, arguments);
                    if (data.length > 0) {
                        data[0] = data[0] + 0.0000001; // Микроскопический шум
                    }
                    return data;
                };
                """

        #Add fonts script to JS
        script += """
                const originalCheck = document.fonts.check;
                document.fonts.check = function(font, text) {
                    const macFonts = ['Helvetica Neue', 'San Francisco', 'Monaco'];
                    const winFonts = ['Segoe UI', 'Calibri', 'Consolas'];

                    // Если профиль Windows, но спрашивают Mac-шрифт - говорим что его нет
                    if ('""" + profile.os_type + """' === 'Windows') {
                        if (macFonts.some(f => font.includes(f))) return false;
                    }
                    // И наоборот
                    if ('""" + profile.os_type + """' === 'macOS') {
                        if (winFonts.some(f => font.includes(f))) return false;
                    }
                    return originalCheck.apply(this, arguments);
                };
                """
        #For mobile
        if profile.os_type in ["Android", "iOS"]:
            script += """
            Object.defineProperty(navigator, 'maxTouchPoints', {get: () => 5});
            window.ontouchstart = null;
            """
        return script