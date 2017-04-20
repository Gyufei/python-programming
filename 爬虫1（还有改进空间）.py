#coding=utf-8
import requests
from bs4 import BeautifulSoup
import os

headers={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
def geturl(url):
    furl=requests.get(url,headers=headers)
    fsuop=BeautifulSoup(furl.text,'lxml')
    return fsuop

def mdir(path):
    path=os.path.join(R'/home/afei/picture',path)
    have=os.path.exists(path)
    if not have:
        print '创建目录：',path
        os.mkdir(path)
        os.chdir(path)
        return True
    else:
        return False

def getimg():
    f=geturl('http://www.mzitu.com/all')
    image_group=f.find('div',class_='all').find_all('a')
    for i in image_group:
        mdir(i.get_text())
        href=i.get('href')
        s=geturl(href)
        maxspan=s.find('div',class_='pagenavi').find_all('span')[-2].get_text()
        for i in range(1,int(maxspan)-1):
            imag_url=href+'/'+str(i)
            s=geturl(imag_url)
            b=s.find('div',class_='main-image').find('img')['src']
            g=requests.get(b,headers=headers)
            filep=open(b[-9:-4]+'.jpg','ab')
            filep.write(g.content)
            filep.close()

getimg()










