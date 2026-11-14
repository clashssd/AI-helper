"""AI-helper/browser_engine/session_manager.py"""
import json
import logging

logger = logging.getLogger(__name__)


def save_cookies_to_json(driver, filepath="cookies.json"):
    """Save cookies to a json file"""
    cookies = driver.get_cookies()
    with open(filepath, 'w') as f:
        json.dump(cookies, f, indent=4)
    logger.info(f"Cookies saved to {filepath}")
    return cookies


def load_cookies_from_json(driver, filepath="cookies.json"):
    """Load cookies from a json file"""
    try:
        with open(filepath, 'r') as f:
            cookies = json.load(f)

        for cookie in cookies:
            driver.add_cookie(cookie)
        logger.info(f"Cookies loaded from {filepath}")
    except FileNotFoundError:
        logger.warning(f"Cookie file {filepath} not found.")