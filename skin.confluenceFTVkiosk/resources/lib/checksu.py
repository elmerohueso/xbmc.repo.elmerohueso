import os
import xbmcvfs
import xbmc

skinpath = xbmc.translatePath('special://skin')

def isrooted():
    if xbmcvfs.exists("/system/bin/su") or xbmcvfs.exists("/system/xbin/su"):
        return True
    else:
        xbmcgui.Dialog().ok("Error","Your device is not rooted.")
        return False

def getperm():
    os.system("su -c 'echo rooted > %s/rooted'" % skinpath)
    if xbmcvfs.exists("%s/rooted" % skinpath):
		if xbmc.executebuiltin("!Skin.HasSetting(HasRoot)"):
            xbmc.executebuiltin("Skin.ToggleSetting(HasRoot)")
    else:
        xbmcgui.Dialog().ok("Error","You did not give XBMC SU permissions.  Please try again.")
        
if isrooted():
    getperm()