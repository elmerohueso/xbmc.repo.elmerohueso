import xbmc
import xbmcgui

xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue", "params":{"setting":"videoplayer.usemediacodec","value":false},"id":1}')
xbmc.executeJSONRPC('{"jsonrpc":"2.0","method":"Settings.SetSettingValue", "params":{"setting":"videoplayer.usestagefright","value":true},"id":1}')
xbmcgui.Dialog().ok("Complete","Changes applied.")       