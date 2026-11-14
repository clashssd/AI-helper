"""AI-helper/profile_creator/ProfileSchema.py"""
import uuid
from dataclasses import dataclass, field
from typing import Optional
@dataclass
class ProfileSchema:
    """Base schema profile for BrowserOpen"""
    #Unique profile ID. If not provided, it is generated automatically.
    profile_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    # output dir where chrome storage
    user_data_dir: str = field(default="")
    profile_name: str = field(default ="Default profile")
    #OC and browser
    os_type: str = field(default="Windows")
    user_agent: str = field(default="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/157.0.0.0 Safari/537.36")
    platform: str = field(default="Win32")
    language: str = field(default="en-Us")
    #Screen
    screen_width: int = field(default=1920)
    screen_height: int = field(default=1080)
    color_depth: int = field(default=24)
    pixel_ratio: float = field(default=1.0)
    #System and rendering
    hardware_concurrency: int = field(default=4) #CPU core
    device_memory: int = field(default=4) #Ram in gb
    webgl_vendor: str = field(default="Google Inc. (Nvidia)")
    webgl_renderer: str = field(default="Angle (NVIDIA,NVIDIA GeForce RTX 3060 Direct3D11 vs_5_0 ps_5_0, D3D11)")
    #Network
    timezone: str = field(default="America/New_York")
    proxy: Optional[str] = field(default=None)
    #if need args
    custom_args: list[str] = field(default_factory=list)



