"""tests_browser_engine/test_presets.py"""
import pytest
from browser_engine.profile_creator.Presets import PRESETS

def test_presets_structure():
    """Check the structure of presets"""
    assert len(PRESETS) > 0, "Base is empty"

def test_presets_required_keys():
    """Check the required keys"""
    required_keys = [
        "os_type", "platform", "user_agent", "screen_width",
        "screen_height", "hardware_concurrency", "device_memory", "webgl_renderer"
    ]
    for name, preset in PRESETS.items():
        for key in required_keys:
            assert key in preset, f"In preset '{name}' no key '{key}'"

def test_presets_ram_power_of_two():
    """Check the ram power of two"""
    valid_rams = [2, 4, 8, 16, 32, 64, 128]
    for name, preset in PRESETS.items():
        assert preset["device_memory"] in valid_rams, f"In preset '{name}' unreal Ram"