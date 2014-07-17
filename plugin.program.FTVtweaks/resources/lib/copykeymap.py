import shutil
import xbmcgui
import xbmc
import sys

profilepath = xbmc.translatePath('special://profile')
resourcepath = os.getcwd()[:-4]

def setkeymap(keymap):
	shutil.copy('%s/keymaps/keymap%s.xml' % (resourcepath,keymap), '%s/keymaps/keyboard.xml' % profilepath)
	xbmcgui.Dialog().ok("Complete","Keymap %s has been set." % keymap)

if sys.argv[1] == 'default':
	try:
		os.remove('%s/keymaps/keyboard.xml' % profilepath)
	except OSError:
		pass
	xbmcgui.Dialog().ok("Complete","Reverted to default keymap.")
else:
	setkeymap('%s' % sys.argv[1])
