#coding=utf-8
import requests
from bs4 import BeautifulSoup
import urllib
import time
import re
import random
url = "https://www.zhihu.com/question/22591304/followers"
my_header = {'User-Agent':'Mozilla/5.0 (X11; Linux i686; rv:52.0) Gecko/20100101 Firefox/52.0'}
my_cookies = {'_zap':'37dfb496-b25f-4670-ada1-5f53bb284d7f',
              'q_c1':'e46471b12b94445083bb78e73077c5c8|1489128557000|1489128557000',
              'r_cap_id':"NGRhZmY0MjUwN2ZkNGU2NzhhYjQyN2EyYWEzMzEwMmQ=|1489489617|f4363b4517ccb1140d97e82004397e9e6b462a38",
              'cap_id':"MmIwZTQyZDI4YmZlNGM0YzkyZDA0OThlZjkyZDA1MjY=|1489489617|e9c9cb480a65e7061c4d89a76fc43599d26991fd",'nweb_qa':'heifetz','d_c0':"ABDCMU7SbQuPToRkE6VOLuvOCr7pJRgvYN0=|1489128557",
              '__utma':'51854390.892348745.1490492047.1490492047.1490492047.1',
              '__utmz':'51854390.1490492047.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/question/20899988',
              '_zap':'d2f815bf-9bb6-4124-86ad-f1fe86aca5d7',
              'z_c0':'Mi4wQUFBQS1va2FBQUFBRU1JeFR0SnRDeGNBQUFCaEFsVk42VnZ2V0FEUmI5Ykh4d011Z1N2aUk4M3pXZW1QblZwcF9B|1490492194|4a876da4d5f834b50b2eecee98d51c6e5d82718d',
              '_xsrf':'1b882d5d180c2fcfbc1c15fc9f02f3c6',
              'aliyungf_tc':'AQAAAFKyZQ4GAQ8AwmngKpmcYxbPCpbJ',
              '__utmc':'51854390',
              '__utmv':'51854390.100-1|2=registration_date=20130321=1^3=entry_date=20130321=1'}
regex=re.compile('<img.*?src="(.*?)".*?>')
n=1
for i in xrange(20,3600,20):
    time.sleep(random.uniform(0.5,1))
    data={'start':'','offset':str(i),'_zap':'37dfb496-b25f-4670-ada1-5f53bb284d7f',}
    html = requests.get(url, cookies=my_cookies,headers=my_header,data=data,timeout=10)
    res=re.findall(regex,html.text)
    for j in res:
        n+=1
        path='/home/afei/picture/%s.jpg'%n
        urllib.urlretrieve(j,path)
        time.sleep(random.uniform(0.5,1))


