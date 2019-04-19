import csv
import json
#遍历爬取所有影片信息
import random
import time
import urllib

import pandas as pd
from lxml import etree
import requests

from douban_spider_keshe.xiju_Movie.xiju_url import get_xiju_url_list

for final_url in get_xiju_url_list():
    try:
        # print(final_url)
        time.sleep(random.random() * 3)  # 设置时间间隔休眠
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
            'Referer': 'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action=',
            'Connection': 'close',
            # 151
            # 'Cookie':'bid=YTmCMpU7VFw; gr_user_id=e89f7f05-54dd-48b7-b016-1cbd195fef72; _vwo_uuid_v2=DD062FA23089F729B3D9D0279EE32C888|f8d13e41707d3b501e94e849c4eac737; viewed="25963163"; ll="118090"; __yadk_uid=rfKjYEj2QgfuQ9hJljPMqjKQqNsBfvhS; douban-fav-remind=1; push_noty_num=0; push_doumail_num=0; __utmv=30149280.15436; __utmz=30149280.1553752471.25.7.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ct=y; ap_v=0,6.0; __utma=30149280.78084383.1551104327.1554291807.1554293742.28; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1554293750%2C%22https%3A%2F%2Fwww.douban.com%2Fmisc%2Fsorry%3Foriginal-url%3Dhttps%253A%252F%252Fmovie.douban.com%252Ftyperank%253Ftype_name%253D%2525E5%252589%2525A7%2525E6%252583%252585%2525E7%252589%252587%2526type%253D11%2526interval_id%253D100%253A90%2526action%253D%22%5D; _pk_ses.100001.4cf6=*; __utma=223695111.759236850.1551332018.1554291807.1554293750.26; __utmb=223695111.0.10.1554293750; __utmz=223695111.1554293750.26.8.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/misc/sorry; ps=y; __utmb=30149280.5.10.1554293742; __utmc=30149280; __utmc=223695111; dbcl2="188944022:BZnWQd/zvvI"; ck=fpKY; _pk_id.100001.4cf6=e70bd7ef5bb896fe.1551332017.28.1554295360.1554291807.'

            # 150
            # 'Cookie': 'bid=YTmCMpU7VFw; gr_user_id=e89f7f05-54dd-48b7-b016-1cbd195fef72; _vwo_uuid_v2=DD062FA23089F729B3D9D0279EE32C888|f8d13e41707d3b501e94e849c4eac737; ct=y; viewed="25963163"; ll="118090"; __yadk_uid=rfKjYEj2QgfuQ9hJljPMqjKQqNsBfvhS; douban-fav-remind=1; dbcl2="154361022:9D3tjbsTYkM"; push_noty_num=0; push_doumail_num=0; __utmv=30149280.15436; __utmz=30149280.1553344867.9.6.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=223695111.1553402455.9.6.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ck=khHp; __utmc=30149280; __utmc=223695111; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1553586985%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.78084383.1551104327.1553584746.1553586986.22; __utmb=30149280.0.10.1553586986; __utma=223695111.759236850.1551332018.1553584746.1553586986.20; __utmb=223695111.0.10.1553586986; _pk_id.100001.4cf6=e70bd7ef5bb896fe.1551332017.22.1553586995.1553584904.',
        }

        # //////////////////////////////////////////////////////////////////构建代理
        # proxyHost = "http-cla.abuyun.com"
        # proxyPort = "9030"
        proxyHost = "http-dyn.abuyun.com"
        proxyPort = "9020"
        proxyUser = "HI641Y4G8E60DG8D"
        proxyPass = "37BE74C1CED239C3"
        # proxyUser = "HP2U0E34R54P4X5C"
        # proxyPass = "29C26C8E994C2195"
        # proxyUser = "H4J13Z7E5PX323YC"
        # proxyPass = "8AC6AAB9CCDFE758"
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
        response = requests.get(final_url, headers=headers, proxies=proxies)
        html_str = response.content.decode()
        # print("可以访问网页")
        # print(html_str)              # 检验是否可访问网页
        html = etree.HTML(html_str)
        # xiju_info = html.xpath('/html//div[@class="info"]/span/a')
        xiju_director = html.xpath('//span[@class="attrs"]/a[1]/text()')
        try:
            xiju_director_director = xiju_director[0]
            xiju_director_screenwriter = xiju_director[1]
            xiju_type = html.xpath('//span[@property="v:genre"]/text()')
            xiju_runtime_list = html.xpath('//span[@property="v:runtime"]/text()')
            xiju_runtime = xiju_runtime_list[0]
            xiju_year = html.xpath('//span[@class="year"]/text()')
            year = xiju_year[0].strip('(').strip(')')
            xiju_name_list = html.xpath('//span[@property="v:itemreviewed"]/text()')
            xiju_name = xiju_name_list[0]
            xiju_info_list = html.xpath('//div[@id="info"]//text()')  # 倒数第20位是地区
            score = html.xpath('//div[@class="rating_self clearfix"]/strong/text()')  # 分数
            xiju_score = score[0]
            # xiju_area=xiju_area_list[-20]
            area_num = xiju_info_list.index('制片国家/地区:')
            actor_num = xiju_info_list.index('主演')
            language_num = xiju_info_list.index('语言:')
            xiju_actor1 = xiju_info_list[actor_num + 2]  # 主演1位置
            xiju_actor2 = xiju_info_list[actor_num + 4]  # 主演2位置
            xiju_actor3 = xiju_info_list[actor_num + 6]  # 主演3位置
            xiju_language = xiju_info_list[language_num + 1]  # 语言位置
            area = area_num + 1
            xiju_area = xiju_info_list[area]  # 地区位置
            area = xiju_area.strip(' ')
            # // span[ @ property = "v:genre"]
            print("-" * 100)
            # print(len(xiju_info))
            print(xiju_director)
            # print(xiju_info_list)
            print("电影名称：", xiju_name)
            print("导演为:", xiju_director_director)
            print("编剧为：", xiju_director_screenwriter)
            print("主演为：", xiju_actor1, xiju_actor2, xiju_actor3)
            print("电影类型：", xiju_type)
            print("片长：", xiju_runtime)
            print("年份:", year)
            print("国家和地区：", area)
            print("语言：", xiju_language)
            print("分数:", xiju_score)
            xijulist = [xiju_name, '', xiju_director_director, '', xiju_director_screenwriter, '',
                          xiju_actor1,
                          '', xiju_actor2, '', xiju_actor3, xiju_type, xiju_runtime, year, area,
                          xiju_language,
                          xiju_score]

            # ..........................................
            # 开始存储CSV
            with open('doubanxiju1000.csv', 'a', encoding='utf-8', newline='') as csvfile:
                writer = csv.writer(csvfile)
                # writer.writerow(['电影名称', '导演', '编剧','主演1','主演2','主演3','电影类型','片长','年份','国家和地区','语言'])
                writer.writerow(xijulist)
        except:
            print("本影片信息丢失")  # 判断影片信息是否存在
            continue
    except:
        continue





