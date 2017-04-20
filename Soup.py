#coding=utf-8
import re

class Tool(object):
    picture=re.compile('<img.*?>| {7}')
    url=re.compile('<a.*?>|</a>')
    tab=re.compile('<tr>|<div>|<div>|</p>')
    biaoge=re.compile('<td>')
    suojin=re.compile('<p.*?>')
    enter=re.compile('<br>|<br><br>')
    qita=re.compile('<.*?>')

    def replace(self,x):
        x=re.sub(self.picture,'',x)
        x=re.sub(self.url,'',x)
        x=re.sub(self.tab,'\n',x)
        x=re.sub(self.biaoge,'\t',x)
        x=re.sub(self.suojin,'\n  ',x)
        x=re.sub(self.enter,'\n',x)
        x=re.sub(self.qita,'',x)
        return x.strip()


