import xbmcaddon
import xbmc
import os

__settings__ = xbmcaddon.Addon(id='script.screensaver.sleepandroid')
__power__ = __settings__.getSetting('powerop')
__logoff__ = __settings__.getSetting('logoffbool')

def logoff():
	xbmc.executebuiltin("System.Logoff()")
	
def sleep():
	os.system("su -c 'input keyevent KEYCODE_POWER'")
	
def poweroff():
	os.system("su -c 'reboot -p'")

if __logoff__ == "true":
	logoff()

if __power__ == "0":
	sleep()
elif __power__ == "1":
	poweroff()
