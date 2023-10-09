"""
Tương tác với module, dùng lệnh AT command để điều khiển module SIM lấy dữ liệu về GPS
"""


def getCurrentGPS():
    """Get current GPS position"""
    # TODO: get real gps from SIM7600G-H jetson nano
    lon, lat = 105.84743666666667, 21.007347222222222
    return lon, lat



