from typing import Dict
from .scpi_strategy import ScpiStrategy
from .oe1022d_strategy import Oe1022dStrategy

def create_strategy(config: Dict):
    device_name = config.get("device_name", "Unknown")
    if device_name == "SMB100A":
        return ScpiStrategy(config)
    elif device_name == "OE1022D":
        return Oe1022dStrategy(config)
    else:
        # Fallback or Error
        raise ValueError(f"Unknown device name: {device_name}")
