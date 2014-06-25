import xbmc
import os

def logoff():
    # Logoff XBMC profile
    xbmc.executebuiltin("System.Logoff()")

    if xbmc.getCondVisibility("system.platform.android"):
        # If running Android, simulate Power button to sleep the device.
        os.system("input keyevent 'KEYCODE_POWER'")
        
logoff()
