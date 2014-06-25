import xbmc
import os

def logoff():
    # Logoff XBMC profile
    xbmc.executebuiltin("System.Logoff()")

    # If running Android, simulate Power button to sleep the device
    if xbmc.getCondVisibility("system.platform.android"):
        os.system("input keyevent 'KEYCODE_POWER'")
        
logoff()
