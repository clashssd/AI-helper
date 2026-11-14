"""tests_browser_engine/test_builder.py"""
import pytest
from browser_engine.profile_creator.BuilderProfile import BuilderProfile

def test_random_preset_selection():
    """Check that preset selection works"""
    preset_name = BuilderProfile.get_random_preset_name()
    assert isinstance(preset_name, str)
    assert len(preset_name) > 0

def test_build_with_custom_name():
    """Check that custom name can be built"""
    profile = BuilderProfile.build_profile(preset_name="win_office_low", custom_name="MyCustomBot")
    assert profile.profile_name == "MyCustomBot"

def test_jitter_does_not_break_ram():
    """Check that ram can be jittered"""
    valid_rams = [4, 8, 16, 32]
    for _ in range(20): # Генерируем 20 раз, чтобы поймать рандом
        profile = BuilderProfile.build_profile(preset_name="win_mid_i5_gtx1650")
        assert profile.device_memory in valid_rams