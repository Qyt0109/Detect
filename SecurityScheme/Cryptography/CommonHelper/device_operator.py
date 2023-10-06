import uuid
import re


def get_mac_address():
    """Get the device's MAC address as a string"""
    try:
        mac_address = uuid.getnode().to_bytes(
            6, byteorder='big')  # b'\x1b\xff\x7f\xc3\xf8\xc6'
        mac_str = "".join(f"{byte:02X}" for byte in mac_address)
        if not validate_mac_address(mac_str):
            raise ValueError("Invalid MAC address")
    except Exception as e:
        raise RuntimeError("Failed to retrieve MAC address") from e
    # Convert the MAC address bytes to a string representation

    return mac_address


def mac_address_to_str(mac_address: bytes) -> str:
    mac_str = "".join(f"{byte:02X}" for byte in mac_address)
    if not validate_mac_address(mac_str):
        raise ValueError("Invalid MAC address")
    return mac_str


def validate_mac_address(mac_address):
    mac_regex = re.compile(r'^[0-9A-F]{12}$')
    return bool(mac_regex.match(mac_address))

# Example usage
# mac_address = DeviceOperator.GetMACAddress()
# print(mac_address)
