import xbmc
import xbmcgui

appname="Pandora"
packagename="com.pandora.android.gtv"

def launcher():
        try:
                xbmc.executebuiltin('XBMC.StartAndroidActivity("%s")' % packagename)
        except:
                xbmcgui.Dialog().ok('App Not Installed', 'The "%s" app (%s) could not be started as it has not been installed.  Please install the "%s" app and try again.' % (appname, packagename, appname))

launcher()
