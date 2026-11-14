"""tests_browser_engine/test_options.py"""
import pytest
from browser_engine.profile_creator.ProfileSchema import ProfileSchema
from browser_engine.profile_creator.OptionsBuilder import OptionsBuilder

@pytest.fixture
def desktop_profile():
    return ProfileSchema(
        os_type="Windows",
        user_agent="TestAgent",
        language="ru-RU,ru;q=0.9",
        screen_width=1920,
        screen_height=1080,
        proxy="http://127.0.0.1:8080",
        hardware_concurrency=8,
        platform="Win32"
    )

@pytest.fixture
def mobile_profile():
    return ProfileSchema(
        os_type="Android",
        platform="Linux armv8l",
        user_agent="MobileAgent"
    )

def test_options_desktop(desktop_profile):
    """Test desktop profile"""
    options = OptionsBuilder.build_options(desktop_profile)
    args = options.arguments
    assert "--user-agent=TestAgent" in args
    assert "--window-size=1920,1180" in args  # 1080 + 100
    assert "--proxy-server=http://127.0.0.1:8080" in args

def test_js_script_desktop(desktop_profile):
    """Test Js script with desktop profile"""
    js = OptionsBuilder.get_js_script(desktop_profile)
    assert "hardwareConcurrency', {get: () => 8}" in js
    assert "platform', {get: () => 'Win32'}" in js
    assert "maxTouchPoints" not in js

def test_js_script_mobile(mobile_profile):
    """JS script test for mobile (must support touch)."""
    js = OptionsBuilder.get_js_script(mobile_profile)
    assert "maxTouchPoints" in js