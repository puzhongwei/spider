#coding=utf-8
import requests
import codecs
from lxml import html
from lxml import etree
import  os,re
import time
import pymongo
headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch, br',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'_user_behavior_=0421f753-481e-4765-ba5d-1724ab418db1; oscid=oFK7%2Bn8AFTbDIwoUMx0%2FjqaizEcjLGGK0sSawThXO5G%2BDoLLtdmsTIO8jDG5XBd3lEvcR7HRr5qypzmd30PKg8Y523vRM2i5EzJnLPnDasZEFz%2BEM%2F07Iz87%2BKOafyqgx7zSa%2FEjwNUNtb8QeK6VkA%3D%3D; Hm_lvt_a411c4d1664dd70048ee98afe7b28f0b=1478488050,1478512945,1478513960,1478566809; Hm_lpvt_a411c4d1664dd70048ee98afe7b28f0b=1478566809',
    'Host':'my.oschina.net',
    'Referer':'https://my.oschina.net/u/136849/home',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36'
        }
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
def getUrl():
    try:
        conn = pymongo.MongoClient('localhost', 27017)
        db = conn.test
    except Exception as e:
        print("连接数据库失败！")
        return
    c = 0
    for i in range(980000, 1000001):
        # 访问网页异常处理
        try:
            s = requests.Session()
            r = s.get('https://my.oschina.net/u/{0}/home'.format(str(i)), headers=headers)
            # r = s.get("https://my.oschina.net/u/3020009/home",headers=headers)
            str1 = 'https://my.oschina.net/u/{0}/home'.format(str(i))
            str2 = r.url
            if str1 == str2:
                pass
            else:
                str1 = str2
            code = r.status_code
            if code == 200:
                pass
                db.Url.insert(
                    {"url": str1}
                )
            else:
                c = c+1
        except Exception as e:
            print(e)
getUrl()
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
