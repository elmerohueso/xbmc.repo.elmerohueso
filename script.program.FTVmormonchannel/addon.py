import xbmc
import xbmcgui
import os

appname="Mormon Channel"
packagename="org.lds.mormonchannel.client.android"

def launcher():
	packagepath = os.popen('pm path %s' % packagename).read()
	if packagepath:
		xbmc.executebuiltin('XBMC.StartAndroidActivity("%s")' % packagename)
	else:
		xbmcgui.Dialog().ok('App Not Installed', 'This is only a shortcut.  Please install the "%s" app (%s) and try again.' % (appname, packagename))

launcher()
