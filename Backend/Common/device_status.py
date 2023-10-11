import socket
import subprocess
from threading import Thread
import time
import psutil

def _extractLast(path):
    parts = path.split("/")  # Split the string by '/'
    last = parts[-1]  # Select the last part of the split string
    return last

def getDiskStatus():
    partitions = psutil.disk_partitions()
    if partitions:
        device_usage_dict = {}  # Initialize an empty dictionary

        for partition in partitions:
            """partition Example
            partition.device = Device: /dev/disk3s6
            partition.mountpoint = /System/Volumes/VM
            """
            usage = psutil.disk_usage(partition.mountpoint)
            """usage Example
            usage.used = Used: 5369208832
            usage.free = Free: 28832661504
            """
            device_key = f"{_extractLast(partition.device)} - {_extractLast(partition.mountpoint)}"
            usage_percent = (usage.used / usage.total) * 100  # Calculate the percentage
            device_usage_dict[device_key] = usage_percent

        # Print the dictionary
        for device, percent in device_usage_dict.items():
            print(f"{device}, {percent:.2f}%")

        return device_usage_dict
    else:
        return None
    
def getCurrentGPS():
    """Get current GPS position"""
    # TODO: get real gps from SIM7600G-H jetson nano
    lon, lat = 105.84743666666667, 21.007347222222222
    return lon, lat
    
def getNetworkStatus():
    network_stats = psutil.net_if_stats()
    network_addrs = psutil.net_if_addrs()

    for interface, stats in network_stats.items():
        print(f"Interface: {interface}")
        print(f"Status: {stats.isup}, Duplex: {stats.duplex}")
        addrs = network_addrs.get(interface, [])
        for addr in addrs:
            print(f"Address family: {addr.family}, Address: {addr.address}")

def getInternetStatus(ip="8.8.8.8", max_attempts=10, retry_interval=1, result_callback=None):
    def _internet_check():
        for _ in range(max_attempts):
            try:
                # Attempt to connect to a well-known server (Google DNS 8.8.8.8)
                socket.create_connection((ip, 53), timeout=5)
                if result_callback:
                    result_callback(True)
                return
            except OSError:
                pass
            time.sleep(retry_interval)
        if result_callback:
            result_callback(False)
    
    internet_check_thread = Thread(target=_internet_check)
    internet_check_thread.start()

# Callback function to handle the result
def _onInternetStatusCheckDone(result):
    if result:
        print("Internet connection is active.")
    else:
        print("No internet connection.")

def getBluetoothStatus():
    #TODO: GET BLUETOOTH STATUS
    return True

# Callback function to handle the result
def _onBluetoothStatusCheckDone(result):
    if result:
        print("Bluetooth is available.")
    else:
        print("Bluetooth is not available.")

def getBatteryStatus():
    battery = psutil.sensors_battery()
    # f"Battery Status: {charging_status}, Battery Percentage: {battery_percent}%"
    return battery.power_plugged, battery.percent # Charging status, battery percent

if __name__ == "__main__":
    # disk_status = getDiskStatus()
    # print(disk_status)
    # network_status = getInternetStatus(result_callback=_onInternetStatusCheckDone)
    # print(network_status)
    getBluetoothStatus(result_callback=_onBluetoothStatusCheckDone)