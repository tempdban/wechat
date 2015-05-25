#-*- coding:utf-8 -*-

import web
import time
import wechat
import gettitle

#import bingq

import simple

from settings import token
from settings import apiurl

urls = (
    apiurl, 'api',
    '/(.*)', 'index'
)


class mwechat(wechat.wechat):
    def textcallback(self):
        if self.Content=='time':
            return self.text(time.asctime())
        elif self.Content[:6]=='title ':
            return self.text(gettitle.gettitle(self.Content[6:]))
#         elif self.Content[:7]=='search ' :
#            return bingq.search(self.Content[7:])
        return self.text(simple.resp(self.Content).decode('utf-8'))


    def subscribecallback(self):
        return self.text(u'欢迎关注，完善功能ing...')

class api:

    def POST(self):
        hove=mwechat()
        return hove.run(web.data())
        

    def GET(self):
        args=web.input()
        try:
            if wechat.checksign(args.timestamp, args.nonce, token ,args.signature)==True:
                return args.echostr
        except :
                raise web.seeother('/')

class index:
    def GET(self ,name):
        return wechat.kpass()

app = web.application(urls, globals())
application = app.wsgifunc()

