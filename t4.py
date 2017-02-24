#coding=utf-8
import requests
import codecs
from lxml import html
from lxml import etree
import  os,re
import time
import pymongo

headers2={
    'Accept':'text/html,*/*;q = 0.01',
    'Accept-Encoding':'gzip, deflate, sdch, br',
    'Accept-Language':'zh - CN, zh;q = 0.8',
    'Connection':'keep-alive',
    'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
    'Cookie':'user_behavior_ = 0421f753-481e-4765-ba5d-1724ab418db1;oscid=oFK7%2Bn8AFTbDIwoUMx0%2FjqaizEcjLGGK0sSawThXO5G%2BDoLLtdmsTIO8jDG5XBd3lEvcR7HRr5qypzmd30PKg8Y523vRM2i5EzJnLPnDasZEFz%2BEM%2F07Iz87%2BKOafyqgx7zSa%2FEjwNUNtb8QeK6VkA%3D%3D;Hm_lvt_a411c4d1664dd70048ee98afe7b28f0b=1478488050,1478512945,1478513960,1478566809',
    'Host':'my.oschina.net',
    'Referer':'https://my.oschina.net/u/136845/home?type=bbs&scope=best',
    'User-Agent':'Mozilla/5.0(X11;Linuxi686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36',
    'X-PJAX':'true',
    'X-PJAX-Container':'# main-article',
    'X-Requested-With':'XMLHttpRequest'
    }

headers3={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch, br',
    'Accept-Language':'zh - CN, zh;q = 0.8',
    'Connection':'keep-alive',
    'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
    'Cookie': '_user_behavior_=0421f753-481e-4765-ba5d-1724ab418db1; oscid=oFK7%2Bn8AFTbDIwoUMx0%2FjqaizEcjLGGK0sSawThXO5G%2BDoLLtdmsTIO8jDG5XBd3lEvcR7HRr5qypzmd30PKg8Y523vRM2i5EzJnLPnDasZEFz%2BEM%2F07Iz87%2BKOafyqgx7zSa%2FEjwNUNtb8QeK6VkA%3D%3D; Hm_lvt_a411c4d1664dd70048ee98afe7b28f0b=1478512945,1478513960,1478566809,1478659805; Hm_lpvt_a411c4d1664dd70048ee98afe7b28f0b=1478669418',
    'Host': 'my.oschina.net',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent': 'Mozilla/5.0(X11;Linuxi686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36',
    }
blog_redcount=[]
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch, br',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '_user_behavior_=0421f753-481e-4765-ba5d-1724ab418db1; oscid=oFK7%2Bn8AFTbDIwoUMx0%2FjqaizEcjLGGK0sSawThXO5G%2BDoLLtdmsTIO8jDG5XBd3lEvcR7HRr5qypzmd30PKg8Y523vRM2i5EzJnLPnDasZEFz%2BEM%2F07Iz87%2BKOafyqgx7zSa%2FEjwNUNtb8QeK6VkA%3D%3D; Hm_lvt_a411c4d1664dd70048ee98afe7b28f0b=1478512945,1478513960,1478566809,1478659805; Hm_lpvt_a411c4d1664dd70048ee98afe7b28f0b=1478674827',
    'Host': 'my.oschina.net',
    'Referer': 'https://my.oschina.net/u/136849/home',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36'
}
s = requests.Session()
#r = s.get('https://my.oschina.net/janpoem?sort=hot', headers=headers3)
r=s.get('https://my.oschina.net/u/2406027',headers=headers)
#r = s.get('https://my.oschina.net/u/136848', headers=headers)
#print(r.status_code)
#print(r.text)
software=[]
for ts in range(1, 10):
    try:
        tree = html.fromstring(r.content.decode('utf-8'))
        s_title = tree.xpath('/html/body/section/section[2]/div[1]/aside/div[1]/div[2]/div/div[{0}]/div/a/div[1]/text()'.format(str(ts)))[0]
        s_describe=tree.xpath('/html/body/section/section[2]/div[1]/aside/div[1]/div[2]/div/div[{0}]/div/a/div[2]/text()'.format(str(ts)))[0]
        s_url=tree.xpath('/html/body/section/section[2]/div[1]/aside/div[1]/div[2]/div/div[{0}]/div/a/@href'.format(str(ts)))[0]
        tmps={"s_title": s_title,"s_describe": s_describe,"s_url":s_url}
        software.append(tmps)
    except Exception as e:
        break
print(software)
