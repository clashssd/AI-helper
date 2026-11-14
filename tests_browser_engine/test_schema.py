"""tests_browser_engine/test_schema.py"""
import pytest
from browser_engine.profile_creator.ProfileSchema import ProfileSchema

def test_schema_defaults():
    """Test defaults"""
    profile = ProfileSchema()
    assert profile.os_type == "Windows"
    assert isinstance(profile.hardware_concurrency, int)
    assert isinstance(profile.screen_width, int)
    assert profile.proxy is None

def test_schema_uuid_uniqueness():
    """Test uuid unique"""
    p1 = ProfileSchema()
    p2 = ProfileSchema()
    assert p1.profile_id != p2.profile_id
    assert len(p1.profile_id) == 36