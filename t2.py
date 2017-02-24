#coding=utf-8
import requests
import codecs
from lxml import html
from lxml import etree
import  os,re
headers={
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip, deflate, sdch, br',
'Accept-Language':'zh-CN,zh;q=0.8',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
'Cookie':'_user_behavior_=0421f753-481e-4765-ba5d-1724ab418db1; oscid=oFK7%2Bn8AFTbDIwoUMx0%2FjqaizEcjLGGK0sSawThXO5G%2BDoLLtdmsTIO8jDG5XBd3lEvcR7HRr5qypzmd30PKg8Y523vRM2i5EzJnLPnDasZEFz%2BEM%2F07Iz87%2BKOafyqgx7zSa%2FEjwNUNtb8QeK6VkA%3D%3D; Hm_lvt_a411c4d1664dd70048ee98afe7b28f0b=1478488050,1478512945,1478513960,1478566809; Hm_lpvt_a411c4d1664dd70048ee98afe7b28f0b=1478566809',
'Host':'my.oschina.net',
'Referer':'https://my.oschina.net/u/136849/home',
'Upgrade-Insecure-Requests':'1',
'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36',
    }
s = requests.Session()

r = s.get('https://my.oschina.net/u/136848/home', headers=headers)


with codecs.open(filename="get.html", mode='w') as f:
    f.write(r.content.decode('utf-8'))

with codecs.open("get.html", 'r', "utf-8") as f:
    info = f.read()

tree=html.fromstring(info)
print(info)

gender=tree.xpath('/html/body/section/section[1]/div/div[1]/a/img/@src')[0]
username=tree.xpath('/html/body/section/section[1]/div/div[2]/div/div/div[1]/a/span/text()')[0]
temp=tree.xpath('/html/body/section/section[1]/div/div[2]/div/div/div[1]/span[1]/text()')[0]
s=str(temp)
campany=s.split('-')
position=s[s.find('-',0)+2:len(s)]
print(position)
location=tree.xpath('/html/body/section/section[1]/div/div[2]/div/div/div[1]/span[2]/text()')[0]
print(location)

