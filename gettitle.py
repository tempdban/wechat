import urllib
import HTMLParser


class parser(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.tiflag = False
        self.title = ""
    def handle_starttag(self, tag, attrs):
        if tag=="title":
            self.tiflag = True
    def handle_endtag(self, tag):
        if tag=="title":
            self.tiflag = False
    def handle_data(self, data):
        if self.tiflag:
            self.title = data

def gettitle(url):
    p=parser()
    data=urllib.urlopen(url).read()
    try:
        data=data.decode("gbk")
    except:
        data=data.decode("utf8")
    p.feed(data)
    return p.title

