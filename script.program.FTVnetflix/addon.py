import xbmc
import xbmcgui
import os

appname="Netflix"
packagename1="org.chromium.content_shell_apk"
packagename2="com.netflix.ninja"

def launcher():
	packagepath1 = os.popen('pm path %s' % packagename1).read()
	packagepath2 = os.popen('pm path %s' % packagename2).read()
	if packagepath1:
		xbmc.executebuiltin('XBMC.StartAndroidActivity("%s")' % packagename1)
	elif packagepath2:
		xbmc.executebuiltin('XBMC.StartAndroidActivity("%s")' % packagename2)
	else:
		xbmcgui.Dialog().ok('App Not Installed', 'This is only a shortcut.  Please install the "%s" app (%s or %s) and try again.' % (appname, packagename1, packagename2))

launcher()
