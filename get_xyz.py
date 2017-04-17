#coding=utf-8
import requests
import codecs
from lxml import html
from lxml import etree
import  os,re
import time
import pymongo
import json
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


def fun():
    data = {
        'north': '30',
        'west': '0',
        'east': '30',
        'south': '0',
        'mag': '1'
    }
    url = 'http://topex.ucsd.edu/cgi-bin/get_data.cgi'
    s = requests.session()
    r = s.post(url, data=data)
    tmp = r.content.decode('utf-8')
    f = open('/usr/local/spark/gaochen/data4.xyz', 'wb')
    f.write(bytes(tmp, 'UTF-8'))
    f.close()
if __name__ == '__main__':
    fun()

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
