import xbmc

class launcher(xbmc.Monitor):
        xbmc.executebuiltin('XBMC.StartAndroidActivity("org.chromium.content_shell_apk")')

mylauncher = launcher()
del mylauncher
