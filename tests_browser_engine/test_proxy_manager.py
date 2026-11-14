"""tests/test_proxy_manager.py"""
import os
import zipfile
import pytest
from network.ProxyManager import ProxyManager
@pytest.fixture
def mock_proxy_file(tmp_path):
    file_path = tmp_path / "test_proxies.txt"
    content = """
    # Это комментарий, он должен игнорироваться
    127.0.0.1:8080
    user1:pass1@192.168.1.100:3128
    user2:pass2@10.0.0.5:1080
    8.8.8.8:8888
    """
    file_path.write_text(content)
    return str(file_path)
def test_parse_proxy_logic(mock_proxy_file):
    """Test: parsing proxy logic"""
    pm = ProxyManager(mock_proxy_file)
    # Test without auth
    parsed = pm._parse_proxy("1.2.3.4:8080")
    assert parsed["host"] == "1.2.3.4"
    assert parsed["port"] == "8080"
    assert parsed["user"] == ""
    assert parsed["pass"] == ""
    # Test authorization
    parsed_auth = pm._parse_proxy("admin:secret@5.6.7.8:3128")
    assert parsed_auth["host"] == "5.6.7.8"
    assert parsed_auth["port"] == "3128"
    assert parsed_auth["user"] == "admin"
    assert parsed_auth["pass"] == "secret"
def test_load_proxies(mock_proxy_file):
    """Test for file"""
    pm = ProxyManager(mock_proxy_file)
    assert len(pm.proxies) == 4
    assert pm.proxies[0]["host"] == "127.0.0.1"
def test_get_proxy_by_index(mock_proxy_file):
    """Test: getting proxy by index"""
    pm = ProxyManager(mock_proxy_file)
    proxy_0 = pm.get_proxy_by_index(0)
    assert proxy_0["host"] == "127.0.0.1"
    assert proxy_0["port"] == "8080"
    proxy_1 = pm.get_proxy_by_index(1)
    assert proxy_1["host"] == "192.168.1.100"
    assert proxy_1["user"] == "user1"
    assert pm.get_proxy_by_index(99) is None
def test_get_proxy_by_string(mock_proxy_file):
    """Test searching proxies by string"""
    pm = ProxyManager(mock_proxy_file)
    proxy = pm.get_proxy_by_string("8.8.8.8:8888")
    assert proxy is not None
    assert proxy["host"] == "8.8.8.8"
    proxy_full = pm.get_proxy_by_string("user2:pass2@10.0.0.5:1080")
    assert proxy_full is not None
    assert proxy_full["user"] == "user2"
    assert pm.get_proxy_by_string("999.999.999.999:0000") is None
def test_list_proxies_output(mock_proxy_file, capsys):
    pm = ProxyManager(mock_proxy_file)
    pm.list_proxies()
    captured = capsys.readouterr()
    assert "=== Available Proxies ===" in captured.out
    assert "[0] 127.0.0.1:8080" in captured.out
    # Check password safe
    assert "[1] user1:***@192.168.1.100:3128" in captured.out
    assert "pass1" not in captured.out
def test_create_auth_extension(tmp_path):
    """Test validation zip for chrome"""
    proxy_with_auth = {
        "host": "1.1.1.1", "port": "8080", "user": "test_user", "pass": "test_pass", "raw": ""
    }
    # Path for testion
    test_zip_path = str(tmp_path / "test_ext.zip")
    # Generation
    result_path = ProxyManager.create_auth_extension(proxy_with_auth, extension_path=test_zip_path)
    # Check file creation
    assert result_path is not None
    assert os.path.exists(result_path)
    # Check for zip archive
    assert zipfile.is_zipfile(result_path)
    # Check data from proxy
    with zipfile.ZipFile(result_path, 'r') as zf:
        assert "manifest.json" in zf.namelist()
        assert "background.js" in zf.namelist()
        bg_js = zf.read("background.js").decode("utf-8")
        assert 'username: "test_user"' in bg_js
        assert 'password: "test_pass"' in bg_js
        assert 'host: "1.1.1.1"' in bg_js
def test_create_auth_extension_no_auth():
    """Test if proxy not have login """
    proxy_no_auth = {"host": "1.1.1.1", "port": "8080", "user": "", "pass": "", "raw": ""}
    result = ProxyManager.create_auth_extension(proxy_no_auth)
    assert result is None