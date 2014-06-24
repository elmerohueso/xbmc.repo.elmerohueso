import xbmc

class launcher(xbmc.Monitor):
        xbmc.executebuiltin('XBMC.StartAndroidActivity("com.hulu.plus")')

mylauncher = launcher()
del mylauncher
