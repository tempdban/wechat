#-*- coding:utf-8 -*-

import urllib2
from xml.dom import minidom
import base64

def search(s):
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    top_level_url = "https://api.datamarket.azure.com/"
    password_mgr.add_password(None, top_level_url, 'tempdban@live.com', '71ky9USaIeN7H+NwOg0/P5L6KRc16vn04dwMbtUb8VI')
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)
    opener = urllib2.build_opener(handler)
    cache=opener.open('https://api.datamarket.azure.com/Bing/Search/v1/Web?Query=%27'+s+'%27').read()
    result=''
    dom = minidom.parseString(cache)
    dom_root = dom.documentElement
    url= dom_root.getElementsByTagName('d:Url')
    title= dom_root.getElementsByTagName('d:Title')
    description= dom_root.getElementsByTagName('d:Description')
#    print '''<a href="%s">%s</a>%s<br/>''' % (url[1].firstChild.data,title[1].firstChild.data,description[1].firstChild.data)
    for a in range(9):
        result+='''<a href="%s">%s</a>%s<br/>''' % (url[a].firstChild.data,title[a].firstChild.data,description[a].firstChild.data)
    return result

