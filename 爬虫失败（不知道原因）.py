import urllib
import re

def cbk(a,b,c):
    per=100*a*b/c
    print  '%.2f%%'%per

def getweb(url):
    page=urllib.urlopen(url)
    web=page.read()
    return web


def getimg(web):
    patt=r'src="(.+?\.jpg)"'
    reg=re.compile(patt)
    imgl=re.findall(reg,web)
    return imgl
    x=0
    for i in imgl:
        local=r'E:\%s.jpg'%x
        urllib.urlretrieve(i,local,cbk)
        x+=1

getimg(getweb('https://tieba.baidu.com/p/4995704456'))