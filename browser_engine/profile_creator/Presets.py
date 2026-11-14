"""AI-helper/profile_creator/Presets.py"""
from typing import Optional, Dict, Any

# A dictionary containing all presets.
# Each key is a unique preset name (e.g., 'win_mid_i5_gtx1650').
PRESETS: Dict[str, Dict[str, Any]] = {

    # WINDOWS 10 presets

    "win_office_low": {
        "profile_name": "Windows Low Office PC",
        "os_type": "Windows", "platform": "Win32",
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "screen_width": 1366, "screen_height": 768, "color_depth": 24, "pixel_ratio": 1.0,
        "hardware_concurrency": 4, "device_memory": 4,
        "webgl_vendor": "Google Inc. (Intel)", "webgl_renderer": "ANGLE (Intel, Intel(R) HD Graphics 630 Direct3D11 vs_5_0 ps_5_0, D3D11)",
        "language": "en-US,en;q=0.9", "timezone": "America/New_York"
    },
    "win_mid_i5_gtx1650": {
        "profile_name": "Windows Mid Gaming",
        "os_type": "Windows", "platform": "Win32",
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "screen_width": 1920, "screen_height": 1080, "color_depth": 24, "pixel_ratio": 1.0,
        "hardware_concurrency": 8, "device_memory": 16,
        "webgl_vendor": "Google Inc. (NVIDIA)", "webgl_renderer": "ANGLE (NVIDIA, NVIDIA GeForce GTX 1650 Direct3D11 vs_5_0 ps_5_0, D3D11)",
        "language": "en-US,en;q=0.9", "timezone": "Europe/London"
    },
    "win_high_rtx3060": {
        "profile_name": "Windows High Gaming",
        "os_type": "Windows", "platform": "Win32",
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "screen_width": 2560, "screen_height": 1440, "color_depth": 24, "pixel_ratio": 1.0,
        "hardware_concurrency": 12, "device_memory": 32,
        "webgl_vendor": "Google Inc. (NVIDIA)", "webgl_renderer": "ANGLE (NVIDIA, NVIDIA GeForce RTX 3060 Direct3D11 vs_5_0 ps_5_0, D3D11)",
        "language": "en-US,en;q=0.9", "timezone": "America/Chicago"
    },
    "win_ultra_rtx4070": {
        "profile_name": "Windows Ultra Gaming",
        "os_type": "Windows", "platform": "Win32",
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "screen_width": 2560, "screen_height": 1440, "color_depth": 32, "pixel_ratio": 1.0,
        "hardware_concurrency": 16, "device_memory": 32,
        "webgl_vendor": "Google Inc. (NVIDIA)", "webgl_renderer": "ANGLE (NVIDIA, NVIDIA GeForce RTX 4070 Direct3D11 vs_5_0 ps_5_0, D3D11)",
        "language": "ru-RU,ru;q=0.9,en-US;q=0.8", "timezone": "Europe/Moscow"
    },
    "win_amd_rx580": {
        "profile_name": "Windows AMD Build",
        "os_type": "Windows", "platform": "Win32",
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "screen_width": 1920, "screen_height": 1080, "color_depth": 24, "pixel_ratio": 1.0,
        "hardware_concurrency": 8, "device_memory": 16,
        "webgl_vendor": "Google Inc. (AMD)", "webgl_renderer": "ANGLE (AMD, AMD Radeon RX 580 Series Direct3D11 vs_5_0 ps_5_0, D3D11)",
        "language": "en-US,en;q=0.9", "timezone": "America/Los_Angeles"
    },
    "win_workstation_quadro": {
        "profile_name": "Windows Workstation",
        "os_type": "Windows", "platform": "Win32",
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "screen_width": 3840, "screen_height": 2160, "color_depth": 24, "pixel_ratio": 1.5,
        "hardware_concurrency": 24, "device_memory": 64,
        "webgl_vendor": "Google Inc. (NVIDIA)", "webgl_renderer": "ANGLE (NVIDIA, NVIDIA Quadro RTX 6000 Direct3D11 vs_5_0 ps_5_0, D3D11)",
        "language": "en-GB,en;q=0.9", "timezone": "Europe/Berlin"
    },
    "win_laptop_intel": {
        "profile_name": "Windows Laptop",
        "os_type": "Windows", "platform": "Win32",
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "screen_width": 1920, "screen_height": 1200, "color_depth": 24, "pixel_ratio": 1.25,
        "hardware_concurrency": 8, "device_memory": 16,
        "webgl_vendor": "Google Inc. (Intel)", "webgl_renderer": "ANGLE (Intel, Intel(R) Iris(R) Xe Graphics Direct3D11 vs_5_0 ps_5_0, D3D11)",
        "language": "en-US,en;q=0.9", "timezone": "Asia/Tokyo"
    },
    "win_old_i3": {
        "profile_name": "Windows Old PC",
        "os_type": "Windows", "platform": "Win32",
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "screen_width": 1600, "screen_height": 900, "color_depth": 24, "pixel_ratio": 1.0,
        "hardware_concurrency": 4, "device_memory": 8,
        "webgl_vendor": "Google Inc. (Intel)", "webgl_renderer": "ANGLE (Intel, Intel(R) HD Graphics 4000 Direct3D11 vs_5_0 ps_5_0, D3D11)",
        "language": "en-US,en;q=0.9", "timezone": "America/New_York"
    },
    "win_ryzen_gtx1080": {
        "profile_name": "Windows Ryzen Gaming",
        "os_type": "Windows", "platform": "Win32",
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "screen_width": 1920, "screen_height": 1080, "color_depth": 24, "pixel_ratio": 1.0,
        "hardware_concurrency": 16, "device_memory": 32,
        "webgl_vendor": "Google Inc. (NVIDIA)", "webgl_renderer": "ANGLE (NVIDIA, NVIDIA GeForce GTX 1080 Direct3D11 vs_5_0 ps_5_0, D3D11)",
        "language": "en-US,en;q=0.9", "timezone": "Europe/Paris"
    },
    "win_4k_rtx3080": {
        "profile_name": "Windows 4K Gaming",
        "os_type": "Windows", "platform": "Win32",
        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "screen_width": 3840, "screen_height": 2160, "color_depth": 32, "pixel_ratio": 2.0,
        "hardware_concurrency": 16, "device_memory": 32,
        "webgl_vendor": "Google Inc. (NVIDIA)", "webgl_renderer": "ANGLE (NVIDIA, NVIDIA GeForce RTX 3080 Direct3D11 vs_5_0 ps_5_0, D3D11)",
        "language": "en-US,en;q=0.9", "timezone": "America/Los_Angeles"
    },


    # MACOS 10 presets

    "mac_m1_air": {
        "profile_name": "MacBook Air M1",
        "os_type": "macOS", "platform": "MacIntel",
        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "screen_width": 1440, "screen_height": 900, "color_depth": 30, "pixel_ratio": 2.0,
        "hardware_concurrency": 8, "device_memory": 8,
        "webgl_vendor": "Apple", "webgl_renderer": "ANGLE (Apple, ANGLE Metal Renderer: Apple M1, Unspecified Version)",
        "language": "en-US,en;q=0.9", "timezone": "America/New_York"
    },
    "mac_m1_pro_14": {
        "profile_name": "MacBook Pro 14 M1 Pro",
        "os_type": "macOS", "platform": "MacIntel",
        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "screen_width": 1512, "screen_height": 982, "color_depth": 30, "pixel_ratio": 2.0,
        "hardware_concurrency": 10, "device_memory": 16,
        "webgl_vendor": "Apple", "webgl_renderer": "ANGLE (Apple, ANGLE Metal Renderer: Apple M1 Pro, Unspecified Version)",
        "language": "en-US,en;q=0.9", "timezone": "America/Los_Angeles"
    },
    "mac_m2_max": {
        "profile_name": "MacBook Pro 16 M2 Max",
        "os_type": "macOS", "platform": "MacIntel",
        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "screen_width": 1728, "screen_height": 1117, "color_depth": 30, "pixel_ratio": 2.0,
        "hardware_concurrency": 12, "device_memory": 32,
        "webgl_vendor": "Apple", "webgl_renderer": "ANGLE (Apple, ANGLE Metal Renderer: Apple M2 Max, Unspecified Version)",
        "language": "en-GB,en;q=0.9", "timezone": "Europe/London"
    },
    "mac_m3_pro": {
        "profile_name": "MacBook Pro 14 M3",
        "os_type": "macOS", "platform": "MacIntel",
        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "screen_width": 1512, "screen_height": 982, "color_depth": 30, "pixel_ratio": 2.0,
        "hardware_concurrency": 11, "device_memory": 16, # ИСПРАВЛЕНО (было 18)
        "webgl_vendor": "Apple", "webgl_renderer": "ANGLE (Apple, ANGLE Metal Renderer: Apple M3 Pro, Unspecified Version)",
        "language": "en-US,en;q=0.9", "timezone": "America/New_York"
    },
    "mac_intel_i9": {
        "profile_name": "MacBook Pro 16 Intel i9",
        "os_type": "macOS", "platform": "MacIntel",
        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "screen_width": 3072, "screen_height": 1920, "color_depth": 30, "pixel_ratio": 2.0,
        "hardware_concurrency": 16, "device_memory": 64,
        "webgl_vendor": "Google Inc. (AMD)", "webgl_renderer": "ANGLE (AMD, AMD Radeon Pro 5500M OpenGL Engine, OpenGL 4.1)",
        "language": "en-US,en;q=0.9", "timezone": "America/Chicago"
    },
    "mac_imac_24": {
        "profile_name": "iMac 24 M1",
        "os_type": "macOS", "platform": "MacIntel",
        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "screen_width": 4480, "screen_height": 2520, "color_depth": 30, "pixel_ratio": 2.0,
        "hardware_concurrency": 8, "device_memory": 8,
        "webgl_vendor": "Apple", "webgl_renderer": "ANGLE (Apple, ANGLE Metal Renderer: Apple M1, Unspecified Version)",
        "language": "en-US,en;q=0.9", "timezone": "Europe/Berlin"
    },
    "mac_mac_mini": {
        "profile_name": "Mac Mini M2",
        "os_type": "macOS", "platform": "MacIntel",
        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "screen_width": 1920, "screen_height": 1080, "color_depth": 24, "pixel_ratio": 1.0,
        "hardware_concurrency": 8, "device_memory": 16,
        "webgl_vendor": "Apple", "webgl_renderer": "ANGLE (Apple, ANGLE Metal Renderer: Apple M2, Unspecified Version)",
        "language": "en-US,en;q=0.9", "timezone": "Asia/Singapore"
    },
    "mac_intel_air": {
        "profile_name": "MacBook Air 2019 Intel",
        "os_type": "macOS", "platform": "MacIntel",
        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "screen_width": 1440, "screen_height": 900, "color_depth": 30, "pixel_ratio": 2.0,
        "hardware_concurrency": 4, "device_memory": 8,
        "webgl_vendor": "Google Inc. (Intel)", "webgl_renderer": "ANGLE (Intel, Intel(R) Iris(TM) Plus Graphics 617 OpenGL Engine, OpenGL 4.1)",
        "language": "en-US,en;q=0.9", "timezone": "America/New_York"
    },
    "mac_pro_m2_ultra": {
        "profile_name": "Mac Studio M2 Ultra",
        "os_type": "macOS", "platform": "MacIntel",
        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "screen_width": 5120, "screen_height": 2880, "color_depth": 30, "pixel_ratio": 2.0,
        "hardware_concurrency": 24, "device_memory": 128,
        "webgl_vendor": "Apple", "webgl_renderer": "ANGLE (Apple, ANGLE Metal Renderer: Apple M2 Ultra, Unspecified Version)",
        "language": "en-US,en;q=0.9", "timezone": "America/Los_Angeles"
    },
    "mac_m1_12": {
        "profile_name": "MacBook 12 M1 (Simulated)",
        "os_type": "macOS", "platform": "MacIntel",
        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "screen_width": 2304, "screen_height": 1440, "color_depth": 30, "pixel_ratio": 2.0,
        "hardware_concurrency": 8, "device_memory": 8,
        "webgl_vendor": "Apple", "webgl_renderer": "ANGLE (Apple, ANGLE Metal Renderer: Apple M1, Unspecified Version)",
        "language": "en-US,en;q=0.9", "timezone": "Europe/Paris"
    },


    # LINUX 10 presets

    "linux_ubuntu_dev": {
        "profile_name": "Ubuntu Developer",
        "os_type": "Linux", "platform": "Linux x86_64",
        "user_agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "screen_width": 1920, "screen_height": 1080, "color_depth": 24, "pixel_ratio": 1.0,
        "hardware_concurrency": 12, "device_memory": 16,
        "webgl_vendor": "Google Inc. (Intel)", "webgl_renderer": "ANGLE (Intel, Mesa Intel(R) UHD Graphics 630 (CFL GT2), OpenGL 4.6)",
        "language": "en-US,en;q=0.9", "timezone": "America/New_York"
    },
    "linux_fedora_amd": {
        "profile_name": "Fedora AMD Workstation",
        "os_type": "Linux", "platform": "Linux x86_64",
        "user_agent": "Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "screen_width": 2560, "screen_height": 1440, "color_depth": 24, "pixel_ratio": 1.0,
        "hardware_concurrency": 16, "device_memory": 32,
        "webgl_vendor": "Google Inc. (AMD)", "webgl_renderer": "ANGLE (AMD, AMD Radeon RX 6700 XT (RADV NAVI22), OpenGL 4.6)",
        "language": "en-US,en;q=0.9", "timezone": "Europe/Berlin"
    },
    "linux_arch_nvidia": {
        "profile_name": "Arch Linux Gaming",
        "os_type": "Linux", "platform": "Linux x86_64",
        "user_agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "screen_width": 2560, "screen_height": 1440, "color_depth": 24, "pixel_ratio": 1.0,
        "hardware_concurrency": 24, "device_memory": 32,
        "webgl_vendor": "Google Inc. (NVIDIA)", "webgl_renderer": "ANGLE (NVIDIA, NVIDIA GeForce RTX 3080/PCIe/SSE2, OpenGL 4.6)",
        "language": "en-US,en;q=0.9", "timezone": "America/Los_Angeles"
    },
    "linux_debian_old": {
        "profile_name": "Debian Server GUI",
        "os_type": "Linux", "platform": "Linux x86_64",
        "user_agent": "Mozilla/5.0 (X11; Debian; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        "screen_width": 1280, "screen_height": 1024, "color_depth": 24, "pixel_ratio": 1.0,
        "hardware_concurrency": 2, "device_memory": 4,
        "webgl_vendor": "Google Inc. (Intel)", "webgl_renderer": "ANGLE (Intel, Mesa Intel(R) HD Graphics 4000 (IVB GT2), OpenGL 4.2)",
        "language": "en-GB,en;q=0.9", "timezone": "Europe/London"
    },
    "linux_thinkpad": {
        "profile_name": "ThinkPad Linux",
        "os_type": "Linux", "platform": "Linux x86_64",
        "user_agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
        "screen_width": 1920, "screen_height": 1080, "color_depth": 24, "pixel_ratio": 1.0,
        "hardware_concurrency": 8, "device_memory": 16,
        "webgl_vendor": "Google Inc. (Intel)", "webgl_renderer": "ANGLE (Intel, Mesa Intel(R) UHD Graphics 620 (KBL GT2), OpenGL 4.6)",
        "language": "en-US,en;q=0.9", "timezone": "Asia/Tokyo"
    },
    "linux_kali": {
        "profile_name": "Kali Linux",
        "os_type": "Linux", "platform": "Linux x86_64",
        "user_agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "screen_width": 1920, "screen_height": 1080, "color_depth": 24, "pixel_ratio": 1.0,
        "hardware_concurrency": 4, "device_memory": 8,
        "webgl_vendor": "Google Inc. (VMware)", "webgl_renderer": "ANGLE (VMware, VMware SVGA 3D Direct3D11 vs_5_0 ps_5_0, D3D11)",
        "language": "en-US,en;q=0.9", "timezone": "Europe/Amsterdam"
    },
    "linux_mint": {
        "profile_name": "Linux Mint",
        "os_type": "Linux", "platform": "Linux x86_64",
        "user_agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "screen_width": 1920, "screen_height": 1200, "color_depth": 24, "pixel_ratio": 1.0,
        "hardware_concurrency": 6, "device_memory": 8,
        "webgl_vendor": "Google Inc. (AMD)", "webgl_renderer": "ANGLE (AMD, Mesa AMD Radeon RX 560 Series (POLARIS11), OpenGL 4.6)",
        "language": "en-US,en;q=0.9", "timezone": "Australia/Sydney"
    },
    "linux_pop_os": {
        "profile_name": "Pop!_OS Dev",
        "os_type": "Linux", "platform": "Linux x86_64",
        "user_agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "screen_width": 2560, "screen_height": 1600, "color_depth": 24, "pixel_ratio": 1.25,
        "hardware_concurrency": 12, "device_memory": 32,
        "webgl_vendor": "Google Inc. (NVIDIA)", "webgl_renderer": "ANGLE (NVIDIA, NVIDIA GeForce GTX 1660 Ti/PCIe/SSE2, OpenGL 4.6)",
        "language": "en-US,en;q=0.9", "timezone": "America/Denver"
    },
    "linux_centos_server": {
        "profile_name": "CentOS Browser",
        "os_type": "Linux", "platform": "Linux x86_64",
        "user_agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        "screen_width": 1024, "screen_height": 768, "color_depth": 24, "pixel_ratio": 1.0,
        "hardware_concurrency": 2, "device_memory": 4,
        "webgl_vendor": "Google Inc. (ATI)", "webgl_renderer": "ANGLE (ATI, AMD ES1000, OpenGL 2.1)",
        "language": "en-US,en;q=0.9", "timezone": "Asia/Kolkata"
    },
    "linux_manjaro": {
        "profile_name": "Manjaro KDE",
        "os_type": "Linux", "platform": "Linux x86_64",
        "user_agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "screen_width": 3440, "screen_height": 1440, "color_depth": 24, "pixel_ratio": 1.0,
        "hardware_concurrency": 16, "device_memory": 32,
        "webgl_vendor": "Google Inc. (AMD)", "webgl_renderer": "ANGLE (AMD, AMD Radeon RX 6900 XT (RADV SIENNA_CICHLID), OpenGL 4.6)",
        "language": "en-US,en;q=0.9", "timezone": "Europe/Warsaw"
    },


    # ANDROID 10 presets

    "android_samsung_s24": {
        "profile_name": "Samsung Galaxy S24 Ultra",
        "os_type": "Android", "platform": "Linux armv8l",
        "user_agent": "Mozilla/5.0 (Linux; Android 14; SM-S928B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
        "screen_width": 412, "screen_height": 915, "color_depth": 24, "pixel_ratio": 3.5,
        "hardware_concurrency": 8, "device_memory": 16, # ИСПРАВЛЕНО (было 12)
        "webgl_vendor": "Qualcomm", "webgl_renderer": "ANGLE (Qualcomm, Adreno (TM) 750, OpenGL ES 3.2)",
        "language": "en-US,en;q=0.9", "timezone": "America/New_York"
    },
    "android_samsung_s23": {
        "profile_name": "Samsung Galaxy S23",
        "os_type": "Android", "platform": "Linux armv8l",
        "user_agent": "Mozilla/5.0 (Linux; Android 13; SM-S911B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
        "screen_width": 360, "screen_height": 780, "color_depth": 24, "pixel_ratio": 3.0,
        "hardware_concurrency": 8, "device_memory": 8,
        "webgl_vendor": "Qualcomm", "webgl_renderer": "ANGLE (Qualcomm, Adreno (TM) 740, OpenGL ES 3.2)",
        "language": "en-GB,en;q=0.9", "timezone": "Europe/London"
    },
    "android_pixel_8_pro": {
        "profile_name": "Google Pixel 8 Pro",
        "os_type": "Android", "platform": "Linux armv8l",
        "user_agent": "Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
        "screen_width": 412, "screen_height": 892, "color_depth": 24, "pixel_ratio": 3.5,
        "hardware_concurrency": 9, "device_memory": 16, # ИСПРАВЛЕНО (было 12)
        "webgl_vendor": "ARM", "webgl_renderer": "ANGLE (ARM, Mali-G715, OpenGL ES 3.2)",
        "language": "en-US,en;q=0.9", "timezone": "America/Los_Angeles"
    },
    "android_pixel_7": {
        "profile_name": "Google Pixel 7",
        "os_type": "Android", "platform": "Linux armv8l",
        "user_agent": "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36",
        "screen_width": 412, "screen_height": 892, "color_depth": 24, "pixel_ratio": 2.625,
        "hardware_concurrency": 8, "device_memory": 8,
        "webgl_vendor": "ARM", "webgl_renderer": "ANGLE (ARM, Mali-G710, OpenGL ES 3.2)",
        "language": "en-US,en;q=0.9", "timezone": "America/Chicago"
    },
    "android_xiaomi_14": {
        "profile_name": "Xiaomi 14 Pro",
        "os_type": "Android", "platform": "Linux armv8l",
        "user_agent": "Mozilla/5.0 (Linux; Android 14; 23116PN5BC) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
        "screen_width": 400, "screen_height": 890, "color_depth": 24, "pixel_ratio": 3.0,
        "hardware_concurrency": 8, "device_memory": 16, # ИСПРАВЛЕНО (было 12)
        "webgl_vendor": "Qualcomm", "webgl_renderer": "ANGLE (Qualcomm, Adreno (TM) 750, OpenGL ES 3.2)",
        "language": "zh-CN,zh;q=0.9,en;q=0.8", "timezone": "Asia/Shanghai"
    },
    "android_oneplus_12": {
        "profile_name": "OnePlus 12",
        "os_type": "Android", "platform": "Linux armv8l",
        "user_agent": "Mozilla/5.0 (Linux; Android 14; CPH2581) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
        "screen_width": 412, "screen_height": 919, "color_depth": 24, "pixel_ratio": 3.5,
        "hardware_concurrency": 8, "device_memory": 16,
        "webgl_vendor": "Qualcomm", "webgl_renderer": "ANGLE (Qualcomm, Adreno (TM) 750, OpenGL ES 3.2)",
        "language": "en-US,en;q=0.9", "timezone": "Asia/Tokyo"
    },
    "android_samsung_a54": {
        "profile_name": "Samsung Galaxy A54",
        "os_type": "Android", "platform": "Linux armv8l",
        "user_agent": "Mozilla/5.0 (Linux; Android 13; SM-A546B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36",
        "screen_width": 384, "screen_height": 854, "color_depth": 24, "pixel_ratio": 2.8,
        "hardware_concurrency": 8, "device_memory": 8, # ИСПРАВЛЕНО (было 6)
        "webgl_vendor": "ARM", "webgl_renderer": "ANGLE (ARM, Mali-G68, OpenGL ES 3.2)",
        "language": "en-US,en;q=0.9", "timezone": "Europe/Berlin"
    },
    "android_xiaomi_redmi": {
        "profile_name": "Xiaomi Redmi Note 12",
        "os_type": "Android", "platform": "Linux armv8l",
        "user_agent": "Mozilla/5.0 (Linux; Android 13; 22111317G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36",
        "screen_width": 393, "screen_height": 873, "color_depth": 24, "pixel_ratio": 2.75,
        "hardware_concurrency": 8, "device_memory": 4,
        "webgl_vendor": "Qualcomm", "webgl_renderer": "ANGLE (Qualcomm, Adreno (TM) 610, OpenGL ES 3.2)",
        "language": "en-US,en;q=0.9", "timezone": "Asia/Kolkata"
    },
    "android_motorola_edge": {
        "profile_name": "Motorola Edge 40",
        "os_type": "Android", "platform": "Linux armv8l",
        "user_agent": "Mozilla/5.0 (Linux; Android 13; moto edge 40) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36",
        "screen_width": 412, "screen_height": 915, "color_depth": 24, "pixel_ratio": 3.0,
        "hardware_concurrency": 8, "device_memory": 8,
        "webgl_vendor": "ARM", "webgl_renderer": "ANGLE (ARM, Mali-G77 MC9, OpenGL ES 3.2)",
        "language": "en-US,en;q=0.9", "timezone": "America/Sao_Paulo"
    },
    "android_sony_xperia": {
        "profile_name": "Sony Xperia 1 V",
        "os_type": "Android", "platform": "Linux armv8l",
        "user_agent": "Mozilla/5.0 (Linux; Android 13; XQ-DQ54) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
        "screen_width": 412, "screen_height": 960, "color_depth": 24, "pixel_ratio": 3.5,
        "hardware_concurrency": 8, "device_memory": 16, # ИСПРАВЛЕНО (было 12)
        "webgl_vendor": "Qualcomm", "webgl_renderer": "ANGLE (Qualcomm, Adreno (TM) 740, OpenGL ES 3.2)",
        "language": "ja-JP,ja;q=0.9,en-US;q=0.8", "timezone": "Asia/Tokyo"
    },

    #IOS 10 presets

    "ios_iphone_15_pro_max": {
        "profile_name": "iPhone 15 Pro Max",
        "os_type": "iOS", "platform": "iPhone",
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1",
        "screen_width": 430, "screen_height": 932, "color_depth": 24, "pixel_ratio": 3.0,
        "hardware_concurrency": 6, "device_memory": 8,
        "webgl_vendor": "Apple", "webgl_renderer": "Apple GPU",
        "language": "en-US,en;q=0.9", "timezone": "America/New_York"
    },
    "ios_iphone_15": {
        "profile_name": "iPhone 15",
        "os_type": "iOS", "platform": "iPhone",
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1",
        "screen_width": 390, "screen_height": 844, "color_depth": 24, "pixel_ratio": 3.0,
        "hardware_concurrency": 6, "device_memory": 8, # ИСПРАВЛЕНО (было 6)
        "webgl_vendor": "Apple", "webgl_renderer": "Apple GPU",
        "language": "en-GB,en;q=0.9", "timezone": "Europe/London"
    },
    "ios_iphone_14_pro": {
        "profile_name": "iPhone 14 Pro",
        "os_type": "iOS", "platform": "iPhone",
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
        "screen_width": 393, "screen_height": 852, "color_depth": 24, "pixel_ratio": 3.0,
        "hardware_concurrency": 6, "device_memory": 8, # ИСПРАВЛЕНО (было 6)
        "webgl_vendor": "Apple", "webgl_renderer": "Apple GPU",
        "language": "en-US,en;q=0.9", "timezone": "America/Los_Angeles"
    },
    "ios_iphone_13": {
        "profile_name": "iPhone 13",
        "os_type": "iOS", "platform": "iPhone",
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1",
        "screen_width": 390, "screen_height": 844, "color_depth": 24, "pixel_ratio": 3.0,
        "hardware_concurrency": 6, "device_memory": 4,
        "webgl_vendor": "Apple", "webgl_renderer": "Apple GPU",
        "language": "en-US,en;q=0.9", "timezone": "America/Chicago"
    },
    "ios_iphone_12_mini": {
        "profile_name": "iPhone 12 Mini",
        "os_type": "iOS", "platform": "iPhone",
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1",
        "screen_width": 375, "screen_height": 812, "color_depth": 24, "pixel_ratio": 3.0,
        "hardware_concurrency": 6, "device_memory": 4,
        "webgl_vendor": "Apple", "webgl_renderer": "Apple GPU",
        "language": "en-GB,en;q=0.9", "timezone": "Europe/Paris"
    },
    "ios_iphone_se": {
        "profile_name": "iPhone SE (3rd gen)",
        "os_type": "iOS", "platform": "iPhone",
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Mobile/15E148 Safari/604.1",
        "screen_width": 375, "screen_height": 667, "color_depth": 24, "pixel_ratio": 2.0,
        "hardware_concurrency": 6, "device_memory": 4,
        "webgl_vendor": "Apple", "webgl_renderer": "Apple GPU",
        "language": "en-US,en;q=0.9", "timezone": "Asia/Singapore"
    },
    "ios_ipad_pro_12": {
        "profile_name": "iPad Pro 12.9 M2",
        "os_type": "iOS", "platform": "MacIntel",
        "user_agent": "Mozilla/5.0 (iPad; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1",
        "screen_width": 1024, "screen_height": 1366, "color_depth": 24, "pixel_ratio": 2.0,
        "hardware_concurrency": 8, "device_memory": 16,
        "webgl_vendor": "Apple", "webgl_renderer": "Apple GPU",
        "language": "en-US,en;q=0.9", "timezone": "America/New_York"
    },
    "ios_ipad_air": {
        "profile_name": "iPad Air 5",
        "os_type": "iOS", "platform": "MacIntel",
        "user_agent": "Mozilla/5.0 (iPad; CPU OS 16_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Mobile/15E148 Safari/604.1",
        "screen_width": 820, "screen_height": 1180, "color_depth": 24, "pixel_ratio": 2.0,
        "hardware_concurrency": 8, "device_memory": 8,
        "webgl_vendor": "Apple", "webgl_renderer": "Apple GPU",
        "language": "en-US,en;q=0.9", "timezone": "Europe/Berlin"
    },
    "ios_iphone_11": {
        "profile_name": "iPhone 11",
        "os_type": "iOS", "platform": "iPhone",
        "user_agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_7 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.7 Mobile/15E148 Safari/604.1",
        "screen_width": 414, "screen_height": 896, "color_depth": 24, "pixel_ratio": 2.0,
        "hardware_concurrency": 6, "device_memory": 4,
        "webgl_vendor": "Apple", "webgl_renderer": "Apple GPU",
        "language": "en-US,en;q=0.9", "timezone": "America/Los_Angeles"
    },
    "ios_ipad_mini": {
        "profile_name": "iPad Mini 6",
        "os_type": "iOS", "platform": "MacIntel",
        "user_agent": "Mozilla/5.0 (iPad; CPU OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.6 Mobile/15E148 Safari/604.1",
        "screen_width": 744, "screen_height": 1133, "color_depth": 24, "pixel_ratio": 2.0,
        "hardware_concurrency": 6, "device_memory": 4,
        "webgl_vendor": "Apple", "webgl_renderer": "Apple GPU",
        "language": "en-GB,en;q=0.9", "timezone": "Australia/Sydney"
    }
}