import xbmcaddon
import xbmc
import os

__settings__ = xbmcaddon.Addon(id='script.screensaver.sleepandroid')
__power__ = __settings__.getSetting('powerop')
__logoff__ = __settings__.getSetting('logoffbool')

if __logoff__ == "true":
	xbmc.executebuiltin("System.Logoff()")

if __power__ == "0":
	os.system("su -c 'input keyevent KEYCODE_POWER'")
elif __power__ == "1":
	os.system("su -c 'reboot -p'")