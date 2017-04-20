#coding=utf-8
import urllib2
import sys
reload(sys)
sys.getdefaultencoding()
import re

pageindex=1
def getpage(url):
    global pageindex
    pageindex+=1
    headers={'User-agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
    result=urllib2.Request(url,headers=headers)
    res=urllib2.urlopen(result)
    read=res.read().decode('utf-8')
    regex=re.compile('<div class="content">\s+<span>(.*?)</span>')
    patch=re.findall(regex,read)
    return patch

readlist=[]
def getnxetpage(page):
    x='http://www.qiushibaike.com/hot/page/'+str(pageindex)
    q=getpage(x)
    for i in q:
        readlist.append(i)
    return readlist

hclist=[]
def zdget():
    print 'nexe---->enter:quit---->q'
    while True:
        if len(readlist)<100:
            hclist.extend(getnxetpage(pageindex))
        s=raw_input()
        if s=='':
            print ('%s'%readlist.pop()).replace('<br/>','\n')
        elif s=='Q':
            break

zdget()
print len(readlist)