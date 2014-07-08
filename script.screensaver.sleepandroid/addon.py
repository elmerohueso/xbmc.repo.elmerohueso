import xbmcgui
import xbmcaddon
import xbmc
import os

__settings__ = xbmcaddon.Addon(id='script.screensaver.sleepandroid')
__power__ = __settings__.getSetting('powerop')
__logoff__ = __settings__.getSetting('logoffbool')

def logoff():
	xbmc.executebuiltin("System.Logoff()")
	
def sleep():
	os.system("su -c 'echo 0 > /sys/devices/virtual/graphics/fb0/cec'")
	os.system("su -c 'input keyevent KEYCODE_POWER'")
	os.system("su -c 'echo 1 > /sys/devices/virtual/graphics/fb0/cec'")
	
def poweroff():
	os.system("su -c 'reboot -p'")

if not xbmc.getCondVisibility("Player.HasAudio"):
	if __logoff__ == "true":
		logoff()

	if __power__ == "0":
		sleep()
	elif __power__ == "1":
		poweroff()
