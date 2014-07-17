import shutil
import xbmcgui
import xbmc
import sys

profilepath = xbmc.translatePath('special://profile')
keypressfalse = '<remoteaskeyboard default="true">false</remoteaskeyboard>'
keypresstrue = '<remoteaskeyboard default="true">true</remoteaskeyboard>'

def searchnreplace(file,oldstring,newstring):
    instance1 = open(file,'r').read()
    instance2 = open(file,'w')
    merge = instance1.replace(oldstring,newstring)
    instance2.write(merge)

if sys.argv[1] == 'remoteaskeyboard':
	searchnreplace('%s/guisettings.xml' % profilepath, keypressfalse, keypresstrue)
	

