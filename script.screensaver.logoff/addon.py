import xbmc
import os

# Logoff XBMC profile
xbmc.executebuiltin("System.Logoff()")

# Simulate Power button to sleep the device.  Do I want to check if the OS is Android, first?
os.system("input keyevent 'KEYCODE_POWER'")
