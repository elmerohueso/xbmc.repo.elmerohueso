# XBMCHUB.com Addon Installer  Module By: Blazetamer-2013-2014
import urllib,urllib2,re,xbmcplugin,xbmcgui,xbmc,xbmcaddon,os,sys,time,shutil
import downloader,extract
addon_id='plugin.program.addoninstaller'
try: 			from addon.common.addon 				import Addon
except:
    try: 		from t0mm0.common.addon import Addon
    except: from t0mm0_common_addon import Addon
addon=Addon(addon_id, sys.argv)
try: 			from addon.common.net 					import Net
except:
    try: 		from t0mm0.common.net import Net
    except: from t0mm0_common_net import Net
net=Net()
settings=xbmcaddon.Addon(id='plugin.program.addoninstaller')
base_url='http://addons.xbmchub.com/'

artPath=xbmc.translatePath(os.path.join('special://home','addons','plugin.program.addoninstaller','resources','art/'))
ADDON=xbmcaddon.Addon(id='plugin.program.addoninstaller')
fanart=artPath+'fanart.jpg'
TxtAddonUpdater='Addon Updater'
ImgAddonUpdater=artPath+'autoupdater.jpg'

def MAININDEX():
    hubpath=xbmc.translatePath(os.path.join('special://home/addons','repository.xbmchub'))
    if not os.path.exists(hubpath): HUBINSTALL('xbmchubrepo','http://offshoregit.com/xbmchub/xbmc-hub-repo/raw/master/repository.xbmchub/repository.xbmchub-1.0.3.zip','','addon','none')
    if settings.getSetting('featured')=='true':
        addDir('Featured Addons','http://tribeca.xbmchub.com/tools/installer/sources/featured-addons.php','featuredindex',artPath+'featuredaddonsa.jpg')
    if settings.getSetting('video')=='true':
        addDir('Video Addons','http://addons.xbmchub.com/category/video/','addonlist',artPath+'movietva.jpg')
    if settings.getSetting('audio')=='true':
        addDir('Audio Addons','http://addons.xbmchub.com/category/audio/','addonlist',artPath+'musica.jpg')
    if settings.getSetting('program')=='true':
        addDir('Program Addons','http://addons.xbmchub.com/category/programs/','programlist',artPath+'programsa.jpg')
    if settings.getSetting('world')=='true':
        addDir('World Section','http://tribeca.xbmchub.com/tools/installer/sources/world.php','worldlist',artPath+'worlda.jpg')
    if settings.getSetting('adult')=='true':
        addDir('Adult Addons','http://tribeca.xbmchub.com/tools/installer/sources/xxx.php','adultlist',artPath+'adultreposa.jpg')
    #addDir('Standalone Addons','none','others',artPath+'other.jpg')
    #addDir('World Standalone Addons','http://tribeca.xbmchub.com/tools/installer/sources/world-solo.php','worldlist',artPath+'world.jpg')
    if settings.getSetting('featured')=='true':
        addDir('Featured Repos','http://tribeca.xbmchub.com/tools/installer/sources/featured-repos.php','featuredaddons',artPath+'featuredrepoa.jpg')
    addDir('Installer Settings','none','settings',artPath+'installersettingsa.jpg')
    addDir('Search by: Addon/Author','http://addons.xbmchub.com/search/?keyword=','searchaddon',artPath+'searcha.jpg')
    addDir(TxtAddonUpdater,'...','autoupdate2',ImgAddonUpdater); 
    ForPrimeWire()
    AUTO_VIEW('list')

def ForPrimeWire():
    html=OPEN_URL('http://tribeca.xbmchub.com/tools/wizard/links.txt').replace('\r','').replace('\n','').replace('\t','').replace('\a',''); #print html
    if ("1CHANNEL" in html):
        match=re.compile('name="(1CHANNEL.*?)"\s*url="(.+?)"\s*img="(.+?)"\s*fanart="(.+?)"').findall(html)[0]; #print match
        if len(match) > 0:
            (name2,url2,img2,fanart2)=match; 
            addDir(name2,url2,'WizardTypeInstaller',img2); 

def WizardTypeInstaller(name,url): MyAddonInstaller(name,url,xbmc.translatePath(os.path.join('special://','home')))
def AddonTypeInstaller(name,url): MyAddonInstaller(name,url,xbmc.translatePath(os.path.join('special://','home','addons')))

def MyAddonInstaller(name,url,ToPath):
    if len(ToPath)==0: return
    path=xbmc.translatePath(os.path.join('special://home','addons','packages'))
    dp=xbmcgui.DialogProgress(); dp.create("Addon Installer","Downloading ",'','Please Wait')
    lib=os.path.join(path,name+'.zip')
    try: os.remove(lib)
    except: pass
    url=FireDrive(url)
    if '[error]' in url: print url; dialog=xbmcgui.Dialog(); dialog.ok("Error!",url); return
    else: print url
    downloader.download(url,lib,dp)
    addonfolder=ToPath
    time.sleep(2)
    dp.update(0,"","Extracting Zip Please Wait")
    print '======================================='; print addonfolder; print '======================================='
    extract.all(lib,addonfolder,dp)
    time.sleep(2)
    xbmc.executebuiltin("XBMC.UpdateLocalAddons()"); 
    dialog=xbmcgui.Dialog(); dialog.ok("Addon Instaler",name+" has been installed","","")
    ##

def OTHERS():
    addDir('General Standalone Addons','http://tribeca.xbmchub.com/tools/installer/sources/general-solo.php','otherlist',artPath+'othera.jpg')
    addDir('World Standalone Addons','http://tribeca.xbmchub.com/tools/installer/sources/world-solo.php','worldlist',artPath+'worlda.jpg')
    #addDir('Adult Addons','http://tribeca.xbmchub.com/tools/installer/sources/xxx.php','adultlist',artPath+'adult.jpg')

def AutoUpdate(url): #Featured Addons
    print url; link=OPEN_URL(url).replace('\r','').replace('\n','').replace('\t','').replace('\a','')
    if "/featured-addons.php" in url:
        match=re.compile('name="(.+?)"url="(.+?)"').findall(link)
        for name,url2 in match:
            itemID=url2[0:-1].split('/')[-1]; print 'checking for addon: '+itemID; 
            path=xbmc.translatePath(os.path.join('special://home/addons',itemID)); 
            AddonDotXml=xbmc.translatePath(os.path.join('special://home/addons',itemID,'addon.xml')); 
            if (os.path.exists(path)==True) and (os.path.isfile(AddonDotXml)==True): print 'path and addon.xml found for: '+itemID; AutoUpdate_ADDONINDEX(name,url2,'addon',itemID); 
            #add2HELPDir(name,url,'addonindex',fanart,fanart,'','addon')
    elif ("/featured-repos.php" in url) or ("/xxx.php" in url):
        match=re.compile("'name' => '(.+?)'.+?downloadUrl' => '(.+?)'").findall(link)
        for name,url2 in match:
            lang='Featured'; name=name.replace('&rsquo;',"'"); name=name.capitalize(); 
            itemID=url2[0:-1].split('/')[-1]; print 'checking for addon: '+itemID; 
            path=xbmc.translatePath(os.path.join('special://home/addons',itemID)); 
            AddonDotXml=xbmc.translatePath(os.path.join('special://home/addons',itemID,'addon.xml')); 
            if (os.path.exists(path)==True) and (os.path.isfile(AddonDotXml)==True): print 'path and addon.xml found for: '+itemID; AutoUpdate_ADDONINDEX(name,url2,'addon',itemID); 
    elif ("/category/programs/" in url) or ("/category/video/" in url) or ("/category/audio/" in url) or ("/category/" in url):
        match=re.compile('<li><a href="(.+?)"><span class="thumbnail"><img src="(.+?)" width="100%" alt="(.+?)"').findall(link)
        for url2,image,name, in match:
            iconimage=base_url+image; 
            itemID=url2[0:-1].split('/')[-1]; print 'checking for addon: '+itemID; 
            path=xbmc.translatePath(os.path.join('special://home/addons',itemID)); 
            AddonDotXml=xbmc.translatePath(os.path.join('special://home/addons',itemID,'addon.xml')); 
            if (os.path.exists(path)==True) and (os.path.isfile(AddonDotXml)==True): print 'path and addon.xml found for: '+itemID; AutoUpdate_ADDONINDEX(name,url2,'addon',itemID); 
    else: print "url type mismatch in attempt to catch the right items match regex string."; return

def AutoUpdate_ADDONINDEX(name,url,filetype,itemID):
    fanart=artPath+'fanart.jpg'; description='No Description available'; print [name,url,filetype,itemID]; 
    path=xbmc.translatePath(os.path.join('special://home/addons',itemID))
    AddonDotXml=xbmc.translatePath(os.path.join('special://home/addons',itemID,'addon.xml'))
    LocalAddonDotXml=File_Open(AddonDotXml).replace('\r','').replace('\a','').replace('\t','').replace('\n',''); 
    LocalVersion=(re.compile('version=["\']([0-9a-zA-Z\.\-]+)["\']\s*').findall(LocalAddonDotXml.split('<addon')[1])[0]).strip(); print "LocalVersion: "+LocalVersion; 
    try: link=OPEN_URL(url); 
    except: print "failed to load url: "+url; return
    itemDirectDownload=re.compile('Direct Download:</strong><br /><a href="(.+?)"').findall(link)[0]
    itemAddonVersion=(re.compile('Version:</strong>(.+?)<br').findall(link)[0]).strip()
    print "RemoteVersion: "+itemAddonVersion; 
    itemRepository=re.compile('Repository:</strong> <a href="(.+?)"').findall(link)[0]
    itemImage=base_url+(re.compile('<img src="(.+?)" alt=".+?" class="pic" /></span>').findall(link)[0])
    itemAuthor=re.compile('Author:</strong> <a href=".+?">(.+?)</a>').findall(link)[0]
    itemAddonName=re.compile('class="pic" /></span>\r\n\t\t\t\t<h2>(.+?)</h2>').findall(link)[0]
    ## ### ##
    ##DO SOMETHING HERE##
    #if not LocalVersion==itemAddonVersion:
    cV=compareVersions(LocalVersion,itemAddonVersion); print cV; 
    if cV=='do_upgrade':
        try:
    		    ADDONINSTALL(itemAddonName,itemDirectDownload,description,filetype,itemRepository,True,itemAddonVersion,LocalVersion)
    		    addHELPDir('AutoUpdated: '+itemAddonName+' - v'+itemAddonVersion,itemDirectDownload,'addoninstall',itemImage,fanart,description,'addon',itemRepository,itemAddonVersion,itemAuthor)
        except: print "error while trying to install: "+itemAddonName; return
    ## ### ##

def compareVersions(LocalV,RemoteV):
    if LocalV==RemoteV: return 'are_equal'
    if ('.' in LocalV) and ('.' in RemoteV):
        try:
            dotL=LocalV.split('.'); 
            dotR=RemoteV.split('.');
        except: return 'do_upgrade'
        try:
            for i in [0,1,2,3]:
                if dotL[i] > dotR[i]: return 'local_greater_than_remote'
        except: return 'do_upgrade'
    return 'do_upgrade'

def FEATUREDINDEX(url): #Featured Addons
    link=OPEN_URL(url).replace('\r','').replace('\n','').replace('\t','')
    match=re.compile('name="(.+?)"url="(.+?)"').findall(link)
    #addDir(TxtAddonUpdater,url,'autoupdate',ImgAddonUpdater); 
    for name,url in match:
        add2HELPDir(name,url,'addonindex',fanart,fanart,'','addon')
    AUTO_VIEW('')

def REPOLIST(url):
    fanart=artPath+'fanart.jpg'
    #mainurl=url
    link=OPEN_URL(url)
    match=re.compile('<li><a href="(.+?)"><span class="thumbnail"><img src="(.+?)" width="100%" alt="(.+?)"').findall(link)
    for url,image,name, in match:
        iconimage=base_url+image
        if 'repo' in name or 'repository' in name or 'Repo' in name or 'Repository' in name:
            add2HELPDir(name,url,'addonindex',iconimage,fanart,'','addon')                   
        nmatch=re.compile('"page last" href="(.+?)"><dfn title="next Page">').findall(link)
    if len(nmatch) > 0:
        addDir('Next Page',(nmatch[0]),'repolist','')    
    AUTO_VIEW('list')    

def ADDONLIST(url):
    fanart=artPath+'fanart.jpg'
    #mainurl=url
    link=OPEN_URL(url)
    match=re.compile('<li><a href="(.+?)"><span class="thumbnail"><img src="(.+?)" width="100%" alt="(.+?)"').findall(link)
    #addDir(TxtAddonUpdater,url,'autoupdate',ImgAddonUpdater); 
    for url,image,name, in match:
        iconimage=base_url+image
        add2HELPDir(name,url,'addonindex',iconimage,fanart,'','addon')                    
        nmatch=re.compile('"page last" href="(.+?)"><dfn title="next Page">').findall(link)
    #WORLDLIST('http://tribeca.xbmchub.com/tools/installer/sources/world-solo.php')
    #OTHERLIST('http://tribeca.xbmchub.com/tools/installer/sources/general-solo.php')   
    #addDir('Standalone Addons','none','others',artPath+'other.jpg')
    if len(nmatch) > 0:
        addDir('Next Page',(nmatch[0]),'addonlistnext','')
    AUTO_VIEW('list')

def PROGRAMLIST(url):
    fanart=artPath+'fanart.jpg'
    #mainurl=url
    link=OPEN_URL(url)
    match=re.compile('<li><a href="(.+?)"><span class="thumbnail"><img src="(.+?)" width="100%" alt="(.+?)"').findall(link)
    #addDir(TxtAddonUpdater,url,'autoupdate',ImgAddonUpdater); 
    for url,image,name, in match:
        iconimage=base_url+image
        add2HELPDir(name,url,'addonindex',iconimage,fanart,'','addon')                    
        nmatch=re.compile('"page last" href="(.+?)"><dfn title="next Page">').findall(link)
    #WORLDLIST('http://tribeca.xbmchub.com/tools/installer/sources/world-solo.php')
    OTHERLIST('http://tribeca.xbmchub.com/tools/installer/sources/general-solo.php')
    #addDir('Standalone Addons','none','others',artPath+'other.jpg')
    if len(nmatch) > 0:
        addDir('Next Page',(nmatch[0]),'addonlistnext','')
    AUTO_VIEW('list')    

def ADDONLISTNEXT(url):
    fanart=artPath+'fanart.jpg'
    #mainurl=url
    link=OPEN_URL(url)
    match=re.compile('<li><a href="(.+?)"><span class="thumbnail"><img src="(.+?)" width="100%" alt="(.+?)"').findall(link)
    #addDir(TxtAddonUpdater,url,'autoupdate',ImgAddonUpdater); 
    for url,image,name, in match:
        iconimage=base_url+image
        add2HELPDir(name,url,'addonindex',iconimage,fanart,'','addon')                    
        nmatch=re.compile('"page last" href="(.+?)"><dfn title="next Page">').findall(link)
    if len(nmatch) > 0:
        addDir('Next Page',(nmatch[0]),'addonlistnext','')
    AUTO_VIEW('list')

def WORLDALONE(url):
    fanart=artPath+'fanart.jpg'
    #mainurl=url
    link=OPEN_URL(url).replace('\r','').replace('\n','').replace('\t','')
    match=re.compile("'name' => '(.+?)','language' => '(.+?)'.+?downloadUrl' => '(.+?)'").findall(link)
    for name,lang,dload in match:
                lang=lang.capitalize()        
                addHELPDir(name+' ('+lang+')',dload,'addoninstall','',fanart,'','addon','none','','')
    #AUTO_VIEW('list')

def WORLDLIST(url):
    fanart=artPath+'fanart.jpg'
    #mainurl=url
    link=OPEN_URL(url).replace('\r','').replace('\n','').replace('\t','')
    match=re.compile("'name' => '(.+?)','language' => '(.+?)'.+?downloadUrl' => '(.+?)'").findall(link)
    AUTO_VIEW('list')
    for name,lang,dload in match:
                lang=lang.capitalize()        
                addHELPDir(name+' ('+lang+')',dload,'addoninstall','',fanart,'','addon','none','','')
    WORLDALONE('http://tribeca.xbmchub.com/tools/installer/sources/world-solo.php')
    #AUTO_VIEW('list')

def OTHERLIST(url):
    fanart=artPath+'fanart.jpg'
    link=OPEN_URL(url).replace('\r','').replace('\n','').replace('\t','')
    match=re.compile("'name' => '(.+?)','type' => '(.+?)'.+?downloadUrl' => '(.+?)'").findall(link)
    #match=re.compile("'name' => '(.+?)'").findall(link)
    if len(match) > 0:
     for name,lang,dload in match:
                lang=lang.capitalize()
                addHELPDir(name +' ('+lang+')' ,dload,'addoninstall','',fanart,'','addon','none','','')
                    #addHELPDir(name,dload,'addoninstall','',fanart,'','addon','none','','')   
                AUTO_VIEW('')

def FEATUREDADDONS(url): #Featured REPOSITORIES
    fanart=artPath+'fanart.jpg'
    #mainurl=url
    link=OPEN_URL(url).replace('\r','').replace('\n','').replace('\t','')
    match=re.compile("'name' => '(.+?)'.+?downloadUrl' => '(.+?)'").findall(link)
    #addDir(TxtAddonUpdater,url,'autoupdate',ImgAddonUpdater); 
    for name,dload in match:
                lang='Featured'
                name=name.replace('&rsquo;',"'")
                name=name.capitalize()
                addHELPDir(name +' ('+lang+')' ,dload,'addoninstall','',fanart,'','addon','none','','')                      
                AUTO_VIEW('')         

def ADULTLIST(url):
    fanart=artPath+'fanart.jpg'
    #mainurl=url
    link=OPEN_URL(url).replace('\r','').replace('\n','').replace('\t','')
    match=re.compile("'name' => '(.+?)'.+?downloadUrl' => '(.+?)'").findall(link)
    #addDir(TxtAddonUpdater,url,'autoupdate',ImgAddonUpdater); 
    for name,dload in match:
                lang='Adults Only'
                addHELPDir(name+' ('+lang+')',dload,'addoninstall','',fanart,'','addon','none','','')                      
                AUTO_VIEW('')               

def ADDONINDEX(name,url,filetype):
    fanart=artPath+'fanart.jpg'; link=OPEN_URL(url); 
    #match=re.compile('<img src="(.+?)" alt=".+?" class="pic" /></span>\r\n\t\t\t\t<h2>(.+?)</h2>\r\n\t\t\t\t<strong>Author:</strong> <a href=".+?">.+?</a><br /><strong>Version:</strong> .+?<br /><strong>Released:</strong> .+?<br /><strong>Repository:</strong> <a href="(.+?)" rel="nofollow">.+?</a><div class="description"><h4>Description:</h4><p> (.+?)</p></div><ul class="addonLinks"><li><strong>Forum Discussion:</strong><br /><a href=".+?" target="_blank"><img src="images/forum.png" alt="Forum discussion" /></a></li><li><strong>Source Code:</strong><br /><img src="images/codebw.png" alt="Source code" /></li><li><strong>Website:</strong><br /><a href=".+?" target="_blank"><img src="images/website.png" alt="Website" /></a></li><li><strong>Direct Download:</strong><br /><a href="(.+?)" rel="nofollow">').findall(link)
    description='Description not available at this time'
    match2=re.compile('<img src="(.+?)" alt=".+?" class="pic" /></span>').findall(link)
    for image in match2:
        match3=re.compile('class="pic" /></span>\r\n\t\t\t\t<h2>(.+?)</h2>').findall(link)
        for name in match3:
            match4=re.compile('Repository:</strong> <a href="(.+?)"').findall(link)
            for repourl in match4:
                link=OPEN_URL(url).replace('\n','').replace('\t','')
                match5=re.compile('Description:</h4><p>(.+?)</p>').findall(link)
                for description in match5:
                    if len(match5) <1:
                            description='No Description available' 
                    link=OPEN_URL(url)     
                    match6=re.compile('Direct Download:</strong><br /><a href="(.+?)"').findall(link)
                    for addonurl in match6:
                        iconimage=base_url+image
                    match7=re.compile('Author:</strong> <a href=".+?">(.+?)</a>').findall(link)
                    for author in match7:
                         match8=re.compile('Version:</strong>(.+?)<br').findall(link)
                         for version in match8:
                             addHELPDir('Install '+name,addonurl,'addoninstall',iconimage,fanart,description,'addon',repourl,version,author)
                             #ADDONINSTALL(name,addonurl,description,'addon',repourl)
                             AUTO_VIEW('addons')

def File_Save(path,data):
    file=open(path,'w')
    file.write(data)
    file.close()

def File_Open(path):
    if os.path.isfile(path): ## File found.
        file=open(path, 'r')
        contents=file.read()
        file.close()
        return contents
    else: return '' ## File not found.

def Note(header="",message="",sleep=5000): xbmc.executebuiltin("XBMC.Notification(%s,%s,%i)" % (header,message,sleep))

def OPEN_URL(url):
  req=urllib2.Request(url)
  req.add_header('User-Agent','Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
  response=urllib2.urlopen(req)
  link=response.read()
  response.close()
  return link

def FireDrive(url):
    if ('http://www.firedrive.com/file/' not in url) and ('http://firedrive.com/file/' not in url) and ('https://www.firedrive.com/file/' not in url) and ('https://firedrive.com/file/' not in url): return url ## contain with current url if not a filedrive url.
    #else:
    try:
        if 'https://' in url: url=url.replace('https://','http://')
        html=net.http_GET(url).content; #print html; 
        if ">This file doesn't exist, or has been removed.<" in html: return "[error]  This file doesn't exist, or has been removed."
        elif ">File Does Not Exist | Firedrive<" in html: return "[error]  File Does Not Exist."
        elif "404: This file might have been moved, replaced or deleted.<" in html: return "[error]  404: This file might have been moved, replaced or deleted."
        data={}; r=re.findall(r'<input\s+type="\D+"\s+name="(.+?)"\s+value="(.+?)"\s*/>',html);
        for name,value in r: data[name]=value
        #print data; 
        if len(data)==0: return '[error]  input data not found.'
        html=net.http_POST(url,data).content; #print html
        r=re.search('<a\s+href="(.+?)"\s+target="_blank"\s+id=\'top_external_download\'\s+title=\'Download This File\'\s*>',html)
        if r: 
        	print urllib.unquote_plus(r.group(1)); 
        	return urllib.unquote_plus(r.group(1))
        else: return url+'#[error]'
    except: return url+'#[error]'

def HUBINSTALL(name,url,description,filetype,repourl):
        try: url=FireDrive(url)
        except: print "error in FireDrive() function."
        path=xbmc.translatePath(os.path.join('special://home','addons','packages'))
        dp=xbmcgui.DialogProgress()
        dp.create("First Launch:","Creating Database ",'','Only Shown on First Launch')
        lib=os.path.join(path,name+'.zip')
        try: os.remove(lib)
        except: pass
        downloader.download(url, lib, dp)
        if filetype=='addon':
            addonfolder=xbmc.translatePath(os.path.join('special://','home','addons'))
        time.sleep(2)
        #dp.update(0,"","Installing selections.....")
        print '======================================='
        print addonfolder
        print '======================================='
        extract.all(lib,addonfolder,'')

def DEPENDINSTALL(name,url,description,filetype,repourl):
        #Split Script Depends============================
        files=url.split('/')
        dependname=files[-1:]
        dependname=str(dependname)
        dependname=dependname.replace('[','').replace(']','').replace('"','').replace('[','').replace("'",'').replace(".zip",'')
        #StoprSplit======================================
        path=xbmc.translatePath(os.path.join('special://home','addons','packages'))
        dp=xbmcgui.DialogProgress()
        dp.create("Configuring Requirments:","Downloading and ",'','Installing '+name)
        lib=os.path.join(path,name+'.zip')
        try: os.remove(lib)
        except: pass
        downloader.download(url,lib,dp)
        if filetype=='addon': addonfolder=xbmc.translatePath(os.path.join('special://','home','addons'))
        time.sleep(2)
        #dp.update(0,"","Installing selections.....")
        print '======================================='; print addonfolder; print '======================================='
        extract.all(lib,addonfolder,'')
        #Start Script Depend Search==================================================================
        depends=xbmc.translatePath(os.path.join('special://home','addons',dependname,'addon.xml'))
        source=open(depends,mode='r')
        link=source.read()
        source.close()
        dmatch=re.compile('import addon="(.+?)"').findall(link)
        for requires in dmatch:
            if not 'xbmc.python' in requires:
                print 'Script Requires --- '+requires
                dependspath=xbmc.translatePath(os.path.join('special://home','addons',requires))
                #if not os.path.exists(dependspath): DEPENDINSTALL(requires,'http://addonrepo.com/xbmchub/depends/'+requires+'.zip','','addon','none')
                if not os.path.exists(dependspath): DEPENDINSTALL(requires,'http://tribeca.xbmchub.com/tools/maintenance/modules/'+requires+'.zip','','addon','none')
        #End Script Depend Search====================================================================== 

def ADDONINSTALL(name,url,description,filetype,repourl,Auto=False,v='',vO=''):
  #Start Depend Setup================================================================================  
  print 'Installing Url is '+url
  addonfile=url.split('-')
  newfile=addonfile[0:-1]
  newfile=str(newfile)
  folder=newfile.split('/')
  addonname=folder[-1:]
  addonname=str(addonname)
  addonname=addonname.replace('[','').replace(']','').replace('"','').replace('[','').replace("'",'')
  print 'SOURCE FILE IS '+addonname
  #End of Depend Setup==================================================================================
  path=xbmc.translatePath(os.path.join('special://home','addons','packages'))
  vTag=''
  if len(v)  > 0: vTag+=" v"+v
  if len(vO) > 0: vTag+=" [local v"+vO+"]"
  confirm=xbmcgui.Dialog().yesno("Please Confirm","                Do you wish to install the chosen add-on and","                        its respective repository if needed?              ","              "+name+vTag,"Cancel","Install")
  #if Auto==True: confirm=True
  if confirm: 
        dp=xbmcgui.DialogProgress()
        dp.create("Download Progress:","Downloading your selection ",'','Please Wait')
        lib=os.path.join(path,name+'.zip')
        try: os.remove(lib)
        except: pass
        downloader.download(url,lib,dp)
        if filetype=='addon':
            addonfolder=xbmc.translatePath(os.path.join('special://','home','addons'))
        elif filetype=='media':
             addonfolder=xbmc.translatePath(os.path.join('special://','home'))    
        elif filetype=='main':
             addonfolder=xbmc.translatePath(os.path.join('special://','home'))
        time.sleep(2)
        #dp.update(0,"","Installing selections.....")
        print '======================================='; print addonfolder; print '======================================='
        extract.all(lib,addonfolder,dp)
        try:
            #Start Addon Depend Search==================================================================
            depends=xbmc.translatePath(os.path.join('special://home','addons',addonname,'addon.xml'))
            source=open(depends,mode='r')
            link=source.read()
            source.close()
            dmatch=re.compile('import addon="(.+?)"').findall(link)
            for requires in dmatch:
                if not 'xbmc.python' in requires:
                    print 'Requires --- '+requires
                    dependspath=xbmc.translatePath(os.path.join('special://home/addons',requires))
                    #if not os.path.exists(dependspath): DEPENDINSTALL(requires,'http://addonrepo.com/xbmchub/depends/'+requires+'.zip','','addon','none')
                    if not os.path.exists(dependspath): DEPENDINSTALL(requires,'http://tribeca.xbmchub.com/tools/maintenance/modules/'+requires+'.zip','','addon','none')
        except:pass
            #End Addon Depend Search======================================================================    
        #dialog=xbmcgui.Dialog()
        #dialog.ok("Success!","Please Reboot To Take Effect","    Brought To You By XBMCHUB.COM ")
#start repo dl
        if  'none' not in repourl:
            path=xbmc.translatePath(os.path.join('special://home/addons','packages'))
            dp=xbmcgui.DialogProgress()
            dp.create("Updating Repo if needed:","Configuring Installation ",'',' ')
            lib=os.path.join(path,name+'.zip')
            try: os.remove(lib)
            except: pass
            downloader.download(repourl, lib, '')
            if   filetype=='addon': addonfolder=xbmc.translatePath(os.path.join('special://','home/addons'))
            elif filetype=='media': addonfolder=xbmc.translatePath(os.path.join('special://','home'))
            elif filetype=='main':  addonfolder=xbmc.translatePath(os.path.join('special://','home'))
            time.sleep(2)
            #dp.update(0,"","Checking Installation......")
            print '======================================='; print addonfolder; print '======================================='
            extract.all(lib,addonfolder,dp)
            xbmc.executebuiltin("XBMC.UpdateLocalAddons()")
            dialog=xbmcgui.Dialog()
            if Auto==True: Note("Success!",name+" "+v+" Installed")
            else: dialog.ok("Success!","     Your Selections Have Been Installed","    Brought To You By XBMCHUB.COM ")
        else:
            xbmc.executebuiltin("XBMC.UpdateLocalAddons()")
            dialog=xbmcgui.Dialog()
            if Auto==True: Note("Success!",name+" "+v+" Installed")
            else: dialog.ok("Success!","     Your Selections Have Been Installed","    Brought To You By XBMCHUB.COM ")
        '''confirm=xbmcgui.Dialog().yesno("Success!","                Please Restart To Take Effect","                        Brought To You By XBMCHUB.COM              ","                    ","Later","Restart")
        if confirm: xbmc.executebuiltin('Quit')
        else: pass'''
  else: return

# Set View
def AUTO_VIEW(content):
     if content:
          xbmcplugin.setContent(int(sys.argv[1]),content)
          if settings.getSetting('auto-view')=='true':
               if content=='addons': xbmc.executebuiltin("Container.SetViewMode(%s)" % settings.getSetting('addon_view'))
               else: xbmc.executebuiltin("Container.SetViewMode(%s)" % settings.getSetting('default-view'))

# HELPDIR**************************************************************
def addDir(name,url,mode,thumb):        
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name,iconImage="DefaultFolder.png",thumbnailImage=thumb)
        #liz.setInfo(type="Video",infoLabels={"title":name,"Plot":description})
        try: liz.setProperty("Fanart_Image",fanart)
        except: pass
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok  

def addHELPDir(name,url,mode,iconimage,fanart,description,filetype,repourl,version,author):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)+"&filetype="+urllib.quote_plus(filetype)+"&repourl="+urllib.quote_plus(repourl)+"&author="+urllib.quote_plus(author)+"&version="+urllib.quote_plus(version)
        ok=True
        liz=xbmcgui.ListItem(name,iconImage="DefaultFolder.png",thumbnailImage=iconimage)
        liz.setInfo(type="Video",infoLabels={"title":name,"plot":description})
        liz.setProperty("Fanart_Image",fanart)
        liz.setProperty("Addon.Description",description)
        liz.setProperty("Addon.Creator",author)
        liz.setProperty("Addon.Version",version)
        #properties={'Addon.Description':meta["plot"]}
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=False)
        return ok

def add2HELPDir(name,url,mode,iconimage,fanart,description,filetype):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&fanart="+urllib.quote_plus(fanart)+"&description="+urllib.quote_plus(description)+"&filetype="+urllib.quote_plus(filetype)
        ok=True
        liz=xbmcgui.ListItem(name,iconImage="DefaultFolder.png",thumbnailImage=iconimage)
        liz.setInfo(type="Video",infoLabels={"title":name,"Plot":description})
        liz.setProperty("Fanart_Image",fanart)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok          

#Start Ketboard Function                
def _get_keyboard(default="",heading="",hidden=False):
	""" shows a keyboard and returns a value """
	keyboard=xbmc.Keyboard(default,heading,hidden )
	keyboard.doModal()
	if (keyboard.isConfirmed()):
		return unicode(keyboard.getText(),"utf-8")
	return default

#Start Search Function
def SEARCHADDON(url):
	searchUrl=url 
	vq=_get_keyboard(heading="Search add-ons")
	# if blank or the user cancelled the keyboard, return
	if (not vq): return False,0
	# we need to set the title to our query
	title=urllib.quote_plus(vq)
	searchUrl+=title+'&criteria=title' 
	print "Searching URL: "+searchUrl 
	ADDONLIST(searchUrl)
	AUTO_VIEW('list')

#****************************************************************
def get_params():
        param=[]; paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]; cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'): params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&'); param={}
                for i in range(len(pairsofparams)):
                        splitparams={}; splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2: param[splitparams[0]]=splitparams[1]
        return param
params=get_params(); url=None; name=None; mode=None; year=None; imdb_id=None

try:    iconimage=urllib.unquote_plus(params["iconimage"])
except: pass
try:    fanart=urllib.unquote_plus(params["fanart"])
except: pass
try:    description=urllib.unquote_plus(params["description"])
except: pass
try:    filetype=urllib.unquote_plus(params["filetype"])
except: pass
try:		url=urllib.unquote_plus(params["url"])
except: pass
try:		name=urllib.unquote_plus(params["name"])
except: pass
try:		mode=urllib.unquote_plus(params["mode"])
except: pass
try:    repourl=urllib.unquote_plus(params["repourl"])
except: pass
try:    author=urllib.unquote_plus(params["author"])
except: pass
try:    version=urllib.unquote_plus(params["version"])
except: pass

print "Mode: "+str(mode); print "URL: "+str(url); print "Name: "+str(name)

#if mode==None or url==None or len(url)<1: STATUSCATS()
if mode==None or url==None or len(url)<1: MAININDEX()

#****************************************************************    
try:
	if url: print url
except: pass
if   mode=="addonstatus": 		items=ADDONSTATUS(url)					# 
elif mode=='others': 					items=OTHERS()									# 
elif mode=='settings':  			addon.show_settings()						# Settings
elif mode=='autoupdate': 			items=AutoUpdate(url) 					# Featured
elif mode=='autoupdate2': 		
	AutoUpdate('http://tribeca.xbmchub.com/tools/installer/sources/featured-addons.php')
	AutoUpdate('http://tribeca.xbmchub.com/tools/installer/sources/featured-repos.php') 					# Featured
elif mode=='featuredindex': 	items=FEATUREDINDEX(url) 				# Featured Addons
elif mode=='featuredaddons': 	items=FEATUREDADDONS(url) 			# Featured REPOSITORIES
elif mode=='addonlistnext': 	items=ADDONLISTNEXT(url)				# 
elif mode=='addonlist': 			items=ADDONLIST(url)						# 
elif mode=='programlist': 		items=PROGRAMLIST(url)					# 
elif mode=='worldlist': 			items=WORLDLIST(url)						# 
elif mode=='worldalone': 			items=WORLDALONE(url)						# 
elif mode=='otherlist': 			items=OTHERLIST(url)						# 
elif mode=='repolist': 				items=REPOLIST(url)							# 
elif mode=='searchaddon': 		SEARCHADDON(url)								# 
elif mode=='addonindex': 			ADDONINDEX(name,url,filetype)		# 
elif mode=='getrepolink': 		items=GETREPOLINK(url)					# 
elif mode=='getrepolist': 		items=GETREPOLIST(url)					# 
elif mode=='getaddonlink': 		items=GETADDONLINK(url)					# 
elif mode=='getshorts': 			items=GETSHORTS(url)						# 
elif mode=='getrepo': 				GETREPO(name,url,description,filetype)	# 
elif mode=='getvideolink': 		items=GETVIDEOLINK(url)					# 
elif mode=='getvideo': 				GETVIDEO(name,url,iconimage,description,filetype)							# 
elif mode=='addoninstall': 		ADDONINSTALL(name,url,description,filetype,repourl)						# 
elif mode=='listrepoitems': 	items=LISTREPOITEMS(name,url,description,filetype,repourl)		# 
elif mode=='addshortcuts': 		ADDSHORTCUTS(name,url,description,filetype)	# 
elif mode=='addsource': 			ADDSOURCE(name,url,description,filetype)		# 
elif mode=='playstream': 			PLAYSTREAM(name,url,iconimage,description)	# 
elif mode=='adultlist': 			items=ADULTLIST(url)						# 
elif mode=='adultallow': 			ADULTALLOW(url)									# 
elif mode=='WizardTypeInstaller': 			WizardTypeInstaller(name,url)									# 
elif mode=='AddonTypeInstaller': 			AddonTypeInstaller(name,url)									# 
elif mode=='dependinstall': 	DEPENDINSTALL(name,url,description,filetype,repourl)					# 
xbmcplugin.endOfDirectory(int(sys.argv[1])) 
