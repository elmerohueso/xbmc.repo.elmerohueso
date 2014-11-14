import xbmc
import os

def logoff():
	xbmc.executebuiltin("System.Logoff()")
	
def sleep():
	os.system("su -c 'echo 0 > /sys/devices/virtual/graphics/fb0/cec'")
	os.system("su -c 'input keyevent KEYCODE_POWER'")
	os.system("su -c 'echo 1 > /sys/devices/virtual/graphics/fb0/cec'")
	
def shutdown():
	os.system("su -c 'reboot -p'")

def reboot():
	os.system("su -c 'reboot'")

if sys.argv[1] == 'shutdown':
	shutdown()
elif sys.argv[1] == 'sleep':
	sleep()
elif sys.argv[1] == 'reboot':
	reboot()

