import os
import subprocess
import time
import sys
import ntplib
from datetime import datetime
import ctypes
import platform

def is_windows():
    return platform.system() == "Windows"

def set_system_time(new_time):
    if is_windows():
        # Convert datetime to system time
        new_time = new_time.timetuple()
        time_format = "%Y-%m-%d %H:%M:%S"
        formatted_time = datetime.strftime(datetime(*new_time[:6]), time_format)

        # Set system time using PowerShell
        try:
            subprocess.run(["powershell", "-Command", f"Set-Date -Date '{formatted_time}'"], check=True)
            print(f"System time updated to: {formatted_time}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to set system time: {e}")
            sys.exit(1)
    else:
        print("This function is only implemented for Windows systems.")
        sys.exit(1)

def sync_time_with_ntp():
    try:
        ntp_client = ntplib.NTPClient()
        response = ntp_client.request('pool.ntp.org')
        new_time = datetime.fromtimestamp(response.tx_time)
        print(f"Time retrieved from NTP server: {new_time}")
        set_system_time(new_time)
    except Exception as e:
        print(f"Failed to sync with NTP server: {e}")
        sys.exit(1)

def main():
    if not is_windows():
        print("AlphaDash is designed to work on Windows systems only.")
        sys.exit(1)

    print("Starting AlphaDash: Synchronizing system time with internet atomic clocks...")
    sync_time_with_ntp()

if __name__ == "__main__":
    main()