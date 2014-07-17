import sys
import xbmcaddon
import xbmcgui
import xbmc

__addon__ = xbmcaddon.Addon()
__addonname__ = __addon__.getAddonInfo('name')
__icon__ = __addon__.getAddonInfo('icon')
__path__ = __addon__.getAddonInfo('path')

mygui = xbmcgui.WindowXMLDialog('script-%s-main.xml' % __addonname__, __path__)
mygui.doModal()
del mygui
