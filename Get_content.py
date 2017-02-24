# coding=utf-8
import requests
import pymongo

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch, br',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '_user_behavior_=0421f753-481e-4765-ba5d-1724ab418db1; oscid=oFK7%2Bn8AFTbDIwoUMx0%2FjqaizEcjLGGK0sSawThXO5G%2BDoLLtdmsTIO8jDG5XBd3lEvcR7HRr5qypzmd30PKg8Y523vRM2i5EzJnLPnDasZEFz%2BEM%2F07Iz87%2BKOafyqgx7zSa%2FEjwNUNtb8QeK6VkA%3D%3D; Hm_lvt_a411c4d1664dd70048ee98afe7b28f0b=1478488050,1478512945,1478513960,1478566809; Hm_lpvt_a411c4d1664dd70048ee98afe7b28f0b=1478566809',
    'Host': 'my.oschina.net',
    'Referer': 'https://my.oschina.net/u/136849/home',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36'
}
headers2 = {
    'Accept': 'text/html,*/*;q = 0.01',
    'Accept-Encoding': 'gzip, deflate, sdch, br',
    'Accept-Language': 'zh - CN, zh;q = 0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    'Cookie': '_user_behavior_ = 0421f753-481e-4765-ba5d-1724ab418db1;oscid=oFK7%2Bn8AFTbDIwoUMx0%2FjqaizEcjLGGK0sSawThXO5G%2BDoLLtdmsTIO8jDG5XBd3lEvcR7HRr5qypzmd30PKg8Y523vRM2i5EzJnLPnDasZEFz%2BEM%2F07Iz87%2BKOafyqgx7zSa%2FEjwNUNtb8QeK6VkA%3D%3D;Hm_lvt_a411c4d1664dd70048ee98afe7b28f0b=1478488050,1478512945,1478513960,1478566809',
    'Host': 'my.oschina.net',
    'Referer': 'https://my.oschina.net/u/136848/home?type=bbs&scope=best',
    'User-Agent': 'Mozilla/5.0(X11;Linuxi686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36',
    'X-PJAX': 'true',
    'X-PJAX-Container': '# main-article',
    'X-Requested-With': 'XMLHttpRequest'
}


def get_content():
    conn = pymongo.MongoClient('localhost',27017)
    db = conn.test
    cu = db.Url
    r = cu.find({})
    t3 = 0
    for i in r:
        url = i["url"]
        t3 += 1
        # 请求1
        s = requests.Session()
        r = s.get(url + '?type=bbs&scope=best', headers=headers)
        '''db.content1.insert(
            {"content": r.content.decode('utf-8')}
        )'''
        # 请求2
        s = requests.Session()
        url1 = url.split('home')[0]
        r = s.get(url1 + '/blog/?sort=hot', headers=headers2)
        '''db.content2.insert(
            {"content": r.content.decode('utf-8')}
        )'''
        print(r.content.decode('utf-8'))
        if t3 == 10:
            break
        else:
            pass


get_content()





