import requests
from bs4 import BeautifulSoup
import urllib

def get_img_list(someurl):
    page=requests.get(someurl)
    img_url=BeautifulSoup(page.text,"lxml")
    soup=img_url.find_all('img',class_='productImage')
    img_list=[]
    for i in soup:
        img_list.append(i["src"])
    return img_list

def get_img(all_img,somepath):
    j=1
    for each_url in all_img:
        urllib.urlretrieve('http://how2j.cn/tmall/' + each_url,
                           somepath + 'p%s.jpg'%j   )
        j+=1
    print "done"

url="http://how2j.cn/tmall/forecategory?cid=79"
path=r"/home/afei/picture/"
ss=get_img_list(url)
get_img(ss,path)


