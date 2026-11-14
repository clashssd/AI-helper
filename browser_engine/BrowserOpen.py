"""AI-helper/browser_engine/BrowserOpen.py"""
import logging
import time
import json
from selenium import webdriver
import uuid
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException

#Builder
from .profile_creator.OptionsBuilder import OptionsBuilder
from .profile_creator.ProfileSchema import ProfileSchema
#Proxy
from network.ProxyManager import ProxyManager
#logging conf
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] [%(levelname)s] - %(message)s')
logger = logging.getLogger(__name__)

def run_selenium_engine(url,profile: ProfileSchema = None, proxy: dict = None):
    """selenium engine"""
    logger.info("start selenium engine")
    #Options for selenium
    if profile:
        options = OptionsBuilder.build_options(profile)
        js_script = OptionsBuilder.get_js_script(profile)
    else:
       options = webdriver.ChromeOptions()
       #Turn on when all is ready "options.add_argument('--headless')"
       #Turn off detect automation
       options.add_argument("--disable-blink-features=AutomationControlled")
       options.add_experimental_option("excludeSwitches", ["enable-automation"])
       options.add_experimental_option('useAutomationExtension', False)
       js_script = "Object.defineProperty(navigator, 'webdriver', {get: () => undefined});"
    driver = None
    #Proxy setting
    proxy_ext_path = None
    if proxy:
        logger.info(f"Setting up proxy: {proxy['host']}:{proxy['port']}")
        options.add_argument(f'--proxy-server=http://{proxy["host"]}:{proxy["port"]}')

        if proxy.get("user"):
            ext_filename = f"proxy_auth_{uuid.uuid4().hex}.zip"
            proxy_ext_path = ProxyManager.create_auth_extension(proxy, extension_path=ext_filename)
            if proxy_ext_path:
                options.add_extension(proxy_ext_path)
                logger.info(f"Proxy auth extension loaded from {ext_filename}.")

    try:
        #Initialize driver
        driver = webdriver.Chrome(options=options)
        #Delete track webdriver from navigator
        driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": js_script
        })
        logger.info(f"Switching to {url}")
        driver.get(url)
        #We wait until the body appears
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        status_code = driver.execute_script(
            "return window.performance.getEntriesByType('navigation')[0].responseStatus;"
        )
        if status_code and 200 <= status_code < 400:
            logger.info(f"Successfully. {url} loaded for status: {status_code}")
            return driver
        else:
            logger.warning(
                f"Warning. {url} return status: {status_code}.Maybe this page have WAF or Page is not found?.")
            return driver
    except TimeoutException:
        logger.error(f"Timeout: page {url} didn't load in 30 seconds. Check your internet connection or VPN.")
        if driver: driver.quit()
    except WebDriverException as e:
        logger.exception(f"Error webdriver: {e}")
        if driver: driver.quit()
    except Exception as e:
        logger.exception(f"Unfinded error: {e}")
        if driver: driver.quit()
    finally:
        if proxy_ext_path and os.path.exists(proxy_ext_path):
            os.remove(proxy_ext_path)
            logger.debug("Temporary proxy extension removed.")

def close_selenium_engine(driver):
    """close selenium engine"""
    if driver:
        try:
            logger.info(f"Closing browser at {driver.current_url}")
            driver.quit()
        except Exception as e:
            logger.exception(f"Error while closing browser: {e}")
