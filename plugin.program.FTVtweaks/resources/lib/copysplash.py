import os
import shutil
import xbmcgui
import xbmc
import xbmcvfs
import sys

xbmchome = xbmc.translatePath('special://home')
resourcepath = os.getcwd()[:-4]

def setsplash(screen):
	xbmcvfs.copy('%s/splash/splash%s.png' % (resourcepath,screen), '%s/media/splash.png' % xbmchome)
	xbmcgui.Dialog().ok("Complete","Splashscreen %s has been set." % screen)

if sys.argv[1] == 'default':
	try:
		xbmcvfs.delete('%s/media/splash.png' % xbmchome)
	except OSError:
		pass
	xbmcgui.Dialog().ok("Complete","Reverted to default splashscreen.")
else:
	setsplash('%s' % sys.argv[1])
