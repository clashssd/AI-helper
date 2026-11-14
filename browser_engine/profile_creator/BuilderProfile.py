"""AI-helper/profile_creator/BuilderProfile.py"""
import random
import logging
import copy
from typing import Optional
from .ProfileSchema import ProfileSchema
from .Presets import PRESETS
#logging conf
logger = logging.getLogger(__name__)

class BuilderProfile:
    """Class for creating a profile"""
    @staticmethod
    def get_random_preset_name() -> str:
        """Return a random preset name from Presets.py"""
        return random.choice(list(PRESETS.keys()))

    @staticmethod
    def apply_jitter_to_preset(preset_data: dict) -> dict:
        """Introduces minor, realistic variations to the preset data,
        ensuring that two profiles using the same preset are not identical"""
        data = copy.deepcopy(preset_data)
        os_type = data.get("os_type", "Windows")
        base_cores = data.get("hardware_concurrency", 8)
        if base_cores >= 8:
            data["hardware_concurrency"] = random.choice([base_cores - 2, base_cores, base_cores + 2])

        base_ram = data.get("device_memory", 8)
        ram_pools = {
            4: [4, 8],
            8: [8, 16],
            16: [8, 16, 32],
            32: [16, 32]
        }
        if base_ram in ram_pools:
            data["device_memory"] = random.choice(ram_pools[base_ram])
        #Screen and parameter randomization (desktop only)
        if os_type not in ["Android", "iOS"]:
            #We trim off a few pixels (simulating a browser window)
            if random.random() < 0.7:
                data["screen_width"] -= random.randint(0, 30)
                data["screen_height"] -= random.randint(0, 50)
            if os_type in ["Windows", "Linux"]:
                if random.random() < 0.3:
                    data["pixel_ratio"] = random.choice([1.0, 1.25, 1.5])
                if random.random() < 0.3:
                    data["color_depth"] = random.choice([24, 32])
        #Sync language and time zone
        tz = data.get("timezone", "America/New_York")
        if "Europe/Moscow" in tz or "Europe/Kiev" in tz:
            data["language"] = "ru-RU,ru;q=0.9,en-US;q=0.8"
        elif "Asia/Tokyo" in tz:
            data["language"] = "ja-JP,ja;q=0.9,en-US;q=0.8"
        elif "Europe" in tz:
            data["language"] = "en-GB,en;q=0.9"

        return data
    @classmethod
    def build_profile(cls,preset_name: Optional[str]=None,custom_name:  Optional[str] = None) ->ProfileSchema:
        """
        Creates a ready-to-use ProfileSchema object.
        If a preset name is not specified, a random one is selected.
         """
        if not preset_name:
            preset_name = cls.get_random_preset_name()
        if preset_name not in PRESETS:
            logger.error(f"Preset '{preset_name}' not found. Using random instead.")
            preset_name = cls.get_random_preset_name()
        logger.info(f"Building profile from preset: {preset_name}")
        #Take the raw preset data
        raw_data = PRESETS[preset_name]
        #Apply "noise" (make it unique)
        mutated_data = cls.apply_jitter_to_preset(raw_data)
        #Set the profile name (if a custom one wasn't provided)
        if custom_name:
            mutated_data["profile_name"] = custom_name
        else:
            mutated_data["profile_name"] = f"{raw_data.get('profile_name', 'Profile')} - {random.randint(1000, 9999)}"
        #Create a schema object
        profile = ProfileSchema(**mutated_data)
        logger.debug(f"Generated profile ID: {profile.profile_id} | Name: {profile.profile_name}")
        profile = ProfileSchema(**mutated_data)
        import os
        profile.user_data_dir = os.path.abspath(f"profiles/{profile.profile_id}")
        return profile

