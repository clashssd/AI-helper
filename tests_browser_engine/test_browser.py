"""tests_browser_engine/test_browser.py"""
import pytest
from unittest.mock import patch, MagicMock
from browser_engine.BrowserOpen import run_selenium_engine
from browser_engine.profile_creator.ProfileSchema import ProfileSchema


#  UNIT TESTS (USING MOCKS)
@patch('browser_engine.BrowserOpen.webdriver.Chrome')
def test_browser_launch_mocked(mock_chrome):
    """Test: verify that the function calls driver.get and returns the driver."""
    # Setting up a fake browser
    mock_driver = MagicMock()
    mock_chrome.return_value = mock_driver

    # Setting up a fake status code (200)
    mock_driver.execute_script.return_value = 200

    # Running the function
    url = "https://example.com"
    driver = run_selenium_engine(url)

    # Verifying that the methods were called
    mock_chrome.assert_called_once()
    mock_driver.get.assert_called_once_with(url)
    assert driver is not None
    assert driver == mock_driver


# INTEGRATION TEST
@pytest.mark.integration
def test_browser_real_launch():
    """ Opens an actual Chrome window"""
    profile = ProfileSchema(hardware_concurrency=16)
    driver = run_selenium_engine("https://example.com", profile=profile)

    try:
        assert driver is not None
        # Verifying that the JS script has executed
        cores = driver.execute_script("return navigator.hardwareConcurrency;")
        assert int(cores) == 16
    finally:
        if driver:
            driver.quit()