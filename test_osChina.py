# coding=utf-8
import requests
import codecs
from lxml import html
from lxml import etree
import  os,re
import time
import pymongo
import datetime
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

# http://blog.csdn.net/selectdb/article/details/14523205


def get_unix_time(s=u""):
    if u"天" in s:
        day = s.split(u'天')[0]
        return int(time.mktime(datetime.date(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day-int(day)).timetuple()))
    elif u"月" in s:
        month = s.split(u"个")[0]
        return int(time.mktime(datetime.date(datetime.date.today().year, datetime.date.today().month-int(month), datetime.date.today().day).timetuple()))
    elif u"年" in s:
        year = s.split(u'年')[0]
        return int(time.mktime(datetime.date(datetime.date.today().year-int(year), datetime.date.today().month,  datetime.date.today().day).timetuple()))


def get_unix_time1(s=u""):
    # print(s)
    current_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    day = s.split(' ')[0]
    t1 = day.split('/')
    f1 = 0
    for i in t1:
        f1 +=1
    hour = s.split(' ')[1]
    if u"今天" == day:
        s = current_time.replace('-', '/')+' '+hour+':'+'00'
    elif u"昨天" == day:
        t = current_time.split('-')
        current_time = str(t[0])+'/'+str(t[1])+'/'+str(int(t[2])-1)
        s = current_time+' '+hour + ':00'
    elif u"前天" == day:
        t = current_time.split('-')
        current_time = str(t[0])+'/'+str(t[1])+'/'+str(int(t[2])-2)
        s = current_time + ' ' + hour + ':00'
    elif f1 == 2:
        t = current_time.split('-')
        s = str(t[0]) + '/' + day+' '+hour+':00'
    else:
        s = s + ':'+'00'
    # print(s)
    return int(time.mktime(time.strptime(s, '%Y/%m/%d %H:%M:%S')))


def get1(url=''):
    try:
        conn = pymongo.MongoClient('localhost', 27017)
        db = conn.test
    except Exception as e:
        print("连接数据库失败！")
        return
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
    headers2 = {
    'Accept':'text/html,*/*;q = 0.01',
    'Accept-Encoding':'gzip, deflate, sdch, br',
    'Accept-Language':'zh - CN, zh;q = 0.8',
    'Connection':'keep-alive',
    'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
    'Cookie':'_user_behavior_ = 0421f753-481e-4765-ba5d-1724ab418db1;oscid=oFK7%2Bn8AFTbDIwoUMx0%2FjqaizEcjLGGK0sSawThXO5G%2BDoLLtdmsTIO8jDG5XBd3lEvcR7HRr5qypzmd30PKg8Y523vRM2i5EzJnLPnDasZEFz%2BEM%2F07Iz87%2BKOafyqgx7zSa%2FEjwNUNtb8QeK6VkA%3D%3D;Hm_lvt_a411c4d1664dd70048ee98afe7b28f0b=1478488050,1478512945,1478513960,1478566809',
    'Host':'my.oschina.net',
    'Referer':'https://my.oschina.net/u/136848/home?type=bbs&scope=best',
    'User-Agent':'Mozilla/5.0(X11;Linuxi686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/53.0.2785.143 Chrome/53.0.2785.143 Safari/537.36',
    'X-PJAX':'true',
    'X-PJAX-Container':'# main-article',
    'X-Requested-With':'XMLHttpRequest'
    }
    # 解析出错
    b = 0
    # 访问出错
    c = 0
    gender = ""
    avatar = ""
    username = ""
    company = ""
    location = ""
    position = ""
    point = 0
    follower = 0
    following = 0
    join_date = []
    rec_login_time ={}
    week_visits = 0
    month_visits = 0
    all_visits = 0
    # 个性签名
    signature = ""
    # 熟悉的开发平台
    fam_devplatform = []
    # 专长领域
    expertise = []
    # 软件作品
    software = []
    # 博文阅读数
    blog_readcount = []
    # 最佳答案
    best_answer = []
    for i in range(1, 2):
        # 访问网页异常处理
        try:
            s = requests.Session()
            # r = s.get('https://my.oschina.net/u/{0}/home?type=bbs&scope=best'.format(str(i)), headers=headers)
            r = s.get(url+'?type=bbs&scope=best', headers=headers)
            tree = html.fromstring(r.content.decode('utf-8'))
            # 解析网页异常处理
            try:
                # 元素是否存在异常处理
                try:
                    avatar = tree.xpath('//*[@class="user-icon"]/a/img/@src')[0]
                except Exception as e:
                    avatar = ""
                try:
                    username = tree.xpath('//*[@class="user-info-detail"]/div/a/span/text()')[0]
                except Exception as e:
                    username = ""
                try:
                    temp = tree.xpath('//*[@class="user-info-detail"]/div[1]/span[1]/text()')[0]
                    s1 = str(temp)
                    if('-' in s1):
                        company = s1.split('-')[0]
                        position = s1[s1.find('-', 0) + 2:len(s1)]
                    else:
                        company = ""
                        position = s1
                        # print(position)
                except Exception as e:
                    company = ""
                    position = ""
                try:
                    location = tree.xpath('//*[@class="user-info-detail"]/div[1]/span[2]/text()')[0]
                except Exception as e:
                    location = ""
                # 性别
                try:
                    gender = tree.xpath('/html/body/section/section[1]/div/div[1]/span/@class')[0]
                    gender = str(gender).split(' ')[1]
                except Exception as e:
                    gender = ""
                    print(e)
                # 加入时间
                join_datet = tree.xpath('//*[@id="user-score-pjax"]/div/div[4]/text()')[0]
                t4 = str(join_datet).strip().split(' ')
                join_datet = t4[1]
                tj = int(time.mktime(time.strptime(join_datet, '%Y/%m/%d')))
                tmpj = {"join_date":join_datet, "unix_timestamp": tj}
                join_date.append(tmpj)
                # 最近登录时间
                rec_login_time_t = tree.xpath('//*[@id="user-score-pjax"]/div/div[4]/text()')[0]
                rec_login_time_t = str(rec_login_time_t).strip()
                rec_login_time_t = rec_login_time_t[rec_login_time_t.find(u'录')+2:len(rec_login_time_t)]
                if rec_login_time_t != "":
                    unix_timestamp = get_unix_time1(rec_login_time_t)
                    rec_login_time = {"recent_login_time": rec_login_time_t, "unix_timestamp": unix_timestamp}
                else:
                    rec_login_time = {}

                # 积分
                point = int(tree.xpath('//*[@id="user-score-pjax"]/div/div[1]/a/text()')[0])
                # 粉丝
                follower = int(tree.xpath('//*[@id="user-score-pjax"]/div/div[2]/a/text()')[0])
                # 关注
                following = int(tree.xpath('//*[@id="user-score-pjax"]/div/div[3]/a/text()')[0])
                # 个性签名
                signature = tree.xpath('//*[@class="user-signature"]/span/text()')[0]
                if u'没写' in str(signature):
                    signature = ""
                # 本周访问
                week_visitst = tree.xpath('//*[@class="count-list"]/li[3]/text()')[0]
                week_visits = int(str(week_visitst)[str(week_visitst).find(':')+2:len(str(week_visitst))])
                # 本月访问
                month_visitst = tree.xpath('//*[@class="count-list"]/li[4]/text()')[0]
                month_visits = int(str(month_visitst)[str(month_visitst).find(':') + 2:len(str(month_visitst))])
                # 所有访问
                all_visitst = tree.xpath('//*[@class="count-list"]/li[5]/text()')[0]
                all_visits = int(str(all_visitst)[str(all_visitst).find(':') + 2:len(str(all_visitst))])
                # 熟悉平台
                try:
                    temp = tree.xpath('//div[@class="skills-item"]/p')[0]
                    t2 = 1
                    for k1 in temp.xpath('./span/text()'):
                        if(t2<5):
                            fam_devplatform.append(str(k1))
                            #print (fam_devplatform)
                            t2=t2+1
                        else:
                            break
                    #fam_devplatform=temp
                except Exception as e:
                    fam_devplatform = []

                # 专长领域
                try:
                    temp = tree.xpath('//div[@class="skills-item"]/p')[1]
                    t2=1
                    for k1 in temp.xpath('./span/text()'):
                        if(t2<=3):
                            expertise.append(str(k1))
                            t2=t2+1
                        else:
                            break
                except Exception as e:
                    expertise = []
                # 软件作品
                for ts in range(1, 10):
                    try:
                        s_title = tree.xpath('//*[@class="software-list"]/div[{0}]/div/a/div[1]/text()'.format(str(ts)))[0]
                        s_describe = tree.xpath('//*[@class="software-list"]/div[{0}]/div/a/div[2]/text()'.format(str(ts)))[0]
                        s_url = tree.xpath('//*[@class="software-list"]/div[{0}]/div/a/@href'.format(str(ts)))[0]
                        tmps = {"soft_title": s_title, "soft_describe": s_describe, "soft_url": s_url}
                        software.append(tmps)
                    except Exception as e:
                        break
                # 最佳回答
                for ta in range(1, 4):
                    try:
                        question = tree.xpath('//*[@id="main-anchor"]/div[2]/div[2]/div[{0}]/div[2]/div[2]/div[1]/a/@alt'.format(str(ta)))[0]
                        reply = int(tree.xpath('//*[@id="main-anchor"]/div[2]/div[2]/div[{0}]/div[2]/div[3]/span/span/text()'.format(str(ta)))[0])
                        rep_time = tree.xpath('//*[@id="main-anchor"]/div[2]/div/div[{0}]/div[2]/div[1]/span[2]/text()'.format(str(ta)))[0]
                        unix_timestamp = get_unix_time(rep_time)
                        tempa = {"question": question, "reply": reply, "reply_time": rep_time, "unix_timestamp": unix_timestamp}
                        best_answer.append(tempa)
                    except Exception as e:
                        break
            except Exception as e:
                print(e)
                print("index1")
                b= b+1

            # 博客阅读数
            try:
                s = requests.Session()
                url1 = url.split('home')[0]
                s.get(url1+'/blog/?sort=hot', headers=headers2)
                # r = s.get('https://my.oschina.net/u/136848?sort=hot', headers=headers3)
                tree = html.fromstring(r.content.decode('utf-8'))
                # print(r.content.decode('utf-8'))
                for tm in range(1, 6):
                    try:
                        title = tree.xpath('//*[@id="list"]/div[{0}]/div/div/div[1]/a/text()'.format(str(tm)))[0]
                        read_num = int(tree.xpath('//*[@id="list"]/div[{0}]/div/div/div[2]/ul//li[1]/span/text()'.format(str(tm)))[0])
                        comment_num = int(tree.xpath('//*[@id="list"]/div[{0}]/div/div/div[2]/ul//li[2]/span/text()'.format(str(tm)))[0])
                        com_time = tree.xpath('//*[@id="list"]/div[{0}]/div/div/div[3]/text()'.format(str(tm)))[0]
                        com_time = str(com_time).strip().split(' ')[0]
                        unix_timestamp = int(time.mktime(time.strptime(com_time, '%Y/%m/%d')))
                        tempm = {"title": str(title).strip(), "read_count": read_num, "comment_count": comment_num,
                                 "comment_time": com_time, "unix_timestamp": unix_timestamp}
                        blog_readcount.append(tempm)
                    except Exception as e:
                        break
            except Exception as e:
                print(e)
                print("index4")
                b=b+1
            db.osChinaTest1.insert({"avatar": avatar,
                                   "gender": gender,
                                   "username": username,
                                   "company": company,
                                   "location": location,
                                   "position": position,
                                   "point": point,
                                   "follower": follower,
                                   "following": following,
                                   "join_date": join_date,
                                   "recent_login_time": rec_login_time,
                                   "week_visits": week_visits,
                                   "month_visits": month_visits,
                                   "all_visits": all_visits,
                                   "signature": signature,
                                   "familiar_develop_platform": fam_devplatform,
                                   "expertise": expertise,
                                   "software": software,
                                   "best_answer": best_answer,
                                   "blog_read_count": blog_readcount
                                   })
            fam_devplatform.clear()
            expertise.clear()
            software.clear()
            best_answer.clear()
            blog_readcount.clear()
            join_date.clear()
            rec_login_time.clear()
        except Exception as e:
            c = c+1
            print(e)
    # print("解析网页失败:"+str(b))
    # print("访问网页失败:"+str(c))

con = pymongo.MongoClient('localhost', 27017)
d = con.test
cu = d.Url
r = cu.find({})
t3 = 0
for i in r:
    t3 += 1
    url = i["url"]
    get1(url)
    if t3 == 2:
        break
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
