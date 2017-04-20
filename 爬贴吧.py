#coding=utf-8
import urllib2
import re
import Soup

class BDTB(object):

    def __init__(self,url,see_lz=0):
        self.url=url
        self.see_lz='?see_lz=%d'%see_lz
        self.tool=Soup.Tool()

    def getpage(self,pagenum):
        uuu=self.url+self.see_lz+'&pn=%d'%pagenum
        request=urllib2.Request(uuu)
        result=urllib2.urlopen(request)
        return result

    def gettitle(self):
        page=self.getpage(1).read()
        regex=re.compile('<h3 class=".*?" title=".*?" style=.*?>(.*?)</h3>')
        title=re.search(regex,page)
        return title.group(1).strip()

    def getpnum(self):
        page2=self.getpage(1).read()
        regex2=re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>',re.S)
        pagenum=re.search(regex2,page2)
        return pagenum.group(1)

    def getneirong(self,x):
        page3=self.getpage(x).read()
        regex3=re.compile('<div id="post_content_\d+".*?>(.*?)</div>')
        nr=re.findall(regex3,page3)
        return nr

    def getartice(self):
        allpage=self.getpnum()
        f=open('fly.txt','a')
        for i in range(int(allpage)):
            wzlb=self.getneirong(i)
            for j in wzlb:
                f.write(self.tool.replace(j))
        f.close()


t=BDTB('https://tieba.baidu.com/p/3138733512',1)
t.getartice()
