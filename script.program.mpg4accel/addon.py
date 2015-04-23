import xbmc
import os.path
import xml.etree.cElementTree as ET

filename = os.path.join(xbmc.translatePath('special://profile'), 'advancedsettings.xml')

def addSetting(category, subCategory, setting, value):
	node1 = root.find(category)
	if node1 is None:
		node1 = ET.SubElement(root, category)
	
	node2 = node1.find(subCategory)
	if node2 is None:
		node2 = ET.SubElement(node1, subCategory)
	
	node3 = node2.find(setting)
	if node3 is not None:
		node2.remove(node3)
	ET.SubElement(node2, setting).text = value

def writeSettings():
	tree = ET.ElementTree(root)
	tree.write(filename)

#Initialize the tree
try:
	tree = ET.parse(filename)
	root = tree.getroot()
except:
	root = ET.Element('advancedsettings')

addSetting('video', 'stagefright', 'usemp4codec', '0')
writeSettings()