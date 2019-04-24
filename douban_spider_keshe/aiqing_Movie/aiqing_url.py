import json
# 获取剧情片的所有影片地址，第一遍爬取
import random
import time

import pandas as pd
from lxml import etree
import requests


def get_aiqing_url_list():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'Referer': 'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action=',
        'Connection': 'close',
        # 151
        # 'Cookie':'bid=YTmCMpU7VFw; gr_user_id=e89f7f05-54dd-48b7-b016-1cbd195fef72; _vwo_uuid_v2=DD062FA23089F729B3D9D0279EE32C888|f8d13e41707d3b501e94e849c4eac737; viewed="25963163"; ll="118090"; __yadk_uid=rfKjYEj2QgfuQ9hJljPMqjKQqNsBfvhS; douban-fav-remind=1; push_noty_num=0; push_doumail_num=0; __utmv=30149280.15436; __utmz=30149280.1553752471.25.7.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ct=y; ap_v=0,6.0; __utma=30149280.78084383.1551104327.1554291807.1554293742.28; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1554293750%2C%22https%3A%2F%2Fwww.douban.com%2Fmisc%2Fsorry%3Foriginal-url%3Dhttps%253A%252F%252Fmovie.douban.com%252Ftyperank%253Ftype_name%253D%2525E5%252589%2525A7%2525E6%252583%252585%2525E7%252589%252587%2526type%253D11%2526interval_id%253D100%253A90%2526action%253D%22%5D; _pk_ses.100001.4cf6=*; __utma=223695111.759236850.1551332018.1554291807.1554293750.26; __utmb=223695111.0.10.1554293750; __utmz=223695111.1554293750.26.8.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/misc/sorry; ps=y; __utmb=30149280.5.10.1554293742; __utmc=30149280; __utmc=223695111; dbcl2="188944022:BZnWQd/zvvI"; ck=fpKY; _pk_id.100001.4cf6=e70bd7ef5bb896fe.1551332017.28.1554295360.1554291807.'

        # 150
        # 'Cookie': 'bid=YTmCMpU7VFw; gr_user_id=e89f7f05-54dd-48b7-b016-1cbd195fef72; _vwo_uuid_v2=DD062FA23089F729B3D9D0279EE32C888|f8d13e41707d3b501e94e849c4eac737; ct=y; viewed="25963163"; ll="118090"; __yadk_uid=rfKjYEj2QgfuQ9hJljPMqjKQqNsBfvhS; douban-fav-remind=1; dbcl2="154361022:9D3tjbsTYkM"; push_noty_num=0; push_doumail_num=0; __utmv=30149280.15436; __utmz=30149280.1553344867.9.6.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=223695111.1553402455.9.6.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ck=khHp; __utmc=30149280; __utmc=223695111; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1553586985%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.78084383.1551104327.1553584746.1553586986.22; __utmb=30149280.0.10.1553586986; __utma=223695111.759236850.1551332018.1553584746.1553586986.20; __utmb=223695111.0.10.1553586986; _pk_id.100001.4cf6=e70bd7ef5bb896fe.1551332017.22.1553586995.1553584904.',
    }
    base_url1 = "https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action=&start={}&limit=20"  # 100-90的影片   完成
    base_url2 = "https://movie.douban.com/j/chart/top_list?type=13&interval_id=90%3A80&action=&start={}&limit=20"  # 完成
    base_url3 = "https://movie.douban.com/j/chart/top_list?type=13&interval_id=80%3A70&action=&start={}&limit=20"  # 80-70的影片
    base_url4 = "https://movie.douban.com/j/chart/top_list?type=13&interval_id=70%3A60&action=&start={}&limit=20"
    base_url5 = "https://movie.douban.com/j/chart/top_list?type=13&interval_id=60%3A50&action=&start={}&limit=20"
    base_url6 = "https://movie.douban.com/j/chart/top_list?type=13&interval_id=50%3A40&action=&start={}&limit=20"
    base_url7 = "https://movie.douban.com/j/chart/top_list?type=13&interval_id=40%3A30&action=&start={}&limit=20"
    base_url8 = "https://movie.douban.com/j/chart/top_list?type=13&interval_id=30%3A20&action=&start={}&limit=20"
    base_url9 = "https://movie.douban.com/j/chart/top_list?type=13&interval_id=20%3A10&action=&start={}&limit=20"
    base_url10 = "https://movie.douban.com/j/chart/top_list?type=13&interval_id=10%3A0&action=&start={}&limit=20"
    base_url = [base_url1, base_url2, base_url3, base_url4, base_url5, base_url6, base_url7, base_url8, base_url9,
                base_url10, ]
    # print(base_url)
    num = 0
    aiqing_Movie = []
    while num <= 320:  # num从0 意味着一共20部电影,一般都是每个段位340多电影
        try:
            i = 0
            while i <= 9:  # 第1次设置为2
                try:
                    time.sleep(random.random() * 3)  # 设置时间间隔休眠
                    # //////////////////////////////////////////////////////////////////构建代理
                    # proxyHost = "http-cla.abuyun.com"
                    proxyHost = "http-dyn.abuyun.com"
                    # proxyPort = "9030"
                    # proxyUser = "H4J13Z7E5PX323YC"
                    # proxyPass = "8AC6AAB9CCDFE758"
                    # proxyUser = "HP2U0E34R54P4X5C"
                    # proxyPass = "29C26C8E994C2195"
                    proxyPort = "9020"
                    proxyUser = "HI641Y4G8E60DG8D"
                    proxyPass = "37BE74C1CED239C3"
                    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
                        "host": proxyHost,
                        "port": proxyPort,
                        "user": proxyUser,
                        "pass": proxyPass,
                    }
                    proxies = {
                        "http": proxyMeta,
                        "https": proxyMeta,
                    }

                    # ///////////////////////////////////////////////////////////////////////////////////////
                    # while i <= 9:
                    url = base_url[i].format(num)  # 构造url
                    i += 1
                    print(url)

                    response = requests.get(url, headers=headers, proxies=proxies)
                    html_str = response.content.decode()
                    # print("可以访问网页")
                    print(html_str)  # 检验是否可访问网页

                    html = etree.HTML(html_str)
                    print(html)
                    dict_aiqing = json.loads(html_str)  # 先把对象转换为json才可以操作
                    print(type(dict_aiqing))  # 判断类型  list类型。每个list[]里面都是一个字典
                    aiqing_Movie = aiqing_Movie + dict_aiqing
                    print(len(aiqing_Movie))

                    for aiqing in dict_aiqing:
                        print(aiqing, "\n")
                    # 输出电影信息
                    print("第", i, "轮爬虫")
                except:
                    continue

            # print("前", num , "部剧情片")
            print("每个段位前", num + 20, "部剧情片完成")
            num += 20
        except:
            continue

    print("爬虫结束")
    # 获取到了每一个电影的字典

    j_num = 0

    print(len(aiqing_Movie))
    url_dict_aiqing = []
    title_dict_aiqing = []
    # print(type(aiqing_Movie[2]))
    while j_num < len(aiqing_Movie):
        dict = aiqing_Movie[j_num]
        # url_dict_aiqing[j_num]=dict['url']
        j_num += 1
        url_dict_aiqing.append(dict['url'])
        title_dict_aiqing.append(dict['title'])
        # print(dict['url'])
        print(url_dict_aiqing)
        # 打印url地址
        # print(title_dict_aiqing)
    return url_dict_aiqing


if __name__ == "__main__":
    get_aiqing_url_list()
