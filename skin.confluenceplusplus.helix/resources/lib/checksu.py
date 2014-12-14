import os
import xbmcvfs
import xbmc
import xbmcgui

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
		xbmc.executebuiltin("Skin.SetBool(HasRoot)")
		xbmcgui.Dialog().ok("Success","Kodi has been granted SU permissions.")
	else:
		xbmcgui.Dialog().ok("Error","You did not give Kodi SU permissions.  Please try again.")

if isrooted():
	getperm()