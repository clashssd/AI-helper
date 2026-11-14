"""AI-helper/network/proxy_manager.py"""
import os
import random
import zipfile
import logging

logger = logging.getLogger(__name__)

class ProxyManager:
    def __init__(self, proxy_file="proxies.txt"):
        self.proxy_file = proxy_file
        self.proxies = [] # list with parsed proxies
        self.load_proxies()

    def load_proxies(self):
        """Load and parse proxy"""
        if not os.path.exists(self.proxy_file):
            logger.warning(f"File {self.proxy_file} not found. Running without proxies.")
            return

        with open(self.proxy_file, "r") as f:
            lines = f.read().splitlines()
            for line in lines:
                line = line.strip()
                if line and not line.startswith("#"):
                    self.proxies.append(self._parse_proxy(line))

        logger.info(f"Loaded {len(self.proxies)} proxies from {self.proxy_file}.")

    def list_proxies(self):
        """Return list of proxies with index"""
        if not self.proxies:
            print("List proxy is empty.")
            return

        print("\n=== Available Proxies ===")
        for idx, proxy in enumerate(self.proxies):
            # Hide password
            auth_str = f"{proxy['user']}:***@" if proxy['user'] else ""
            print(f"[{idx}] {auth_str}{proxy['host']}:{proxy['port']}")
        print("===========================\n")

    def get_proxy_by_index(self, index: int) -> dict:
        """Return proxy for index"""
        try:
            proxy = self.proxies[index]
            logger.info(f"Selected proxy by index {index}: {proxy['host']}:{proxy['port']}")
            return proxy
        except IndexError:
            logger.error(f"Proxy index {index} out of range. Total proxies: {len(self.proxies)}")
            return None

    def get_proxy_by_string(self, proxy_str: str) -> dict:
        """find proxy (for example, '123.45.67.89:8080')."""
        for proxy in self.proxies:
            if proxy["raw"] == proxy_str or f"{proxy['host']}:{proxy['port']}" == proxy_str:
                logger.info(f"Selected proxy by string: {proxy_str}")
                return proxy
        logger.warning(f"Proxy '{proxy_str}' not found in list.")
        return None

    def get_random_proxy(self) -> dict:
        """return random proxy if u want"""
        if not self.proxies:
            return None
        proxy = random.choice(self.proxies)
        logger.info(f"Selected random proxy: {proxy['host']}:{proxy['port']}")
        return proxy

    def _parse_proxy(self, proxy_str: str) -> dict:
        """Parse proxy line. Return list with host, port, user, pass."""
        proxy_dict = {"raw": proxy_str, "host": "", "port": "", "user": "", "pass": ""}

        if "@" in proxy_str:
            auth, address = proxy_str.split("@")
            if ":" in auth:
                proxy_dict["user"], proxy_dict["pass"] = auth.split(":", 1)
        else:
            address = proxy_str

        if ":" in address:
            proxy_dict["host"], proxy_dict["port"] = address.split(":", 1)

        return proxy_dict

    @staticmethod
    def create_auth_extension(proxy: dict, extension_path="proxy_auth_plugin.zip"):
        if not proxy.get("user"):
            return None

        manifest_json = """
            {
                "version": "1.0.0",
                "manifest_version": 2,
                "name": "Chrome Proxy",
                "permissions": [
                    "proxy", "tabs", "unlimitedStorage", "storage", "<all_urls>",
                    "webRequest", "webRequestBlocking"
                ],
                "background": { "scripts": ["background.js"] },
                "minimum_chrome_version": "22.0.0"
            }
            """

        background_js = """
            var config = {
                mode: "fixed_servers",
                rules: {
                    singleProxy: {
                        scheme: "http",
                        host: "%s",
                        port: parseInt(%s)
                    },
                    bypassList: ["localhost"]
                }
            };
            chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});
            function callbackFn(details) {
                return {
                    authCredentials: {
                        username: "%s",
                        password: "%s"
                    }
                };
            }
            chrome.webRequest.onAuthRequired.addListener(
                callbackFn,
                {urls: ["<all_urls>"]},
                ['blocking']
            );
            """ % (proxy["host"], proxy["port"], proxy["user"], proxy["pass"])

        with zipfile.ZipFile(extension_path, 'w') as zp:
            zp.writestr("manifest.json", manifest_json)
            zp.writestr("background.js", background_js)

        return os.path.abspath(extension_path)