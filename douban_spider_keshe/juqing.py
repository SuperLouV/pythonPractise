import json

import pandas as pd
from lxml import etree
import requests


def get_juqing_url_list():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'Referer': 'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action=',

        'Cookie': 'bid=YTmCMpU7VFw; gr_user_id=e89f7f05-54dd-48b7-b016-1cbd195fef72; _vwo_uuid_v2=DD062FA23089F729B3D9D0279EE32C888|f8d13e41707d3b501e94e849c4eac737; ct=y; viewed="25963163"; ll="118090"; __yadk_uid=rfKjYEj2QgfuQ9hJljPMqjKQqNsBfvhS; douban-fav-remind=1; dbcl2="154361022:9D3tjbsTYkM"; push_noty_num=0; push_doumail_num=0; __utmv=30149280.15436; __utmz=30149280.1553344867.9.6.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=223695111.1553402455.9.6.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ck=khHp; __utmc=30149280; __utmc=223695111; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1553586985%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.78084383.1551104327.1553584746.1553586986.22; __utmb=30149280.0.10.1553586986; __utma=223695111.759236850.1551332018.1553584746.1553586986.20; __utmb=223695111.0.10.1553586986; _pk_id.100001.4cf6=e70bd7ef5bb896fe.1551332017.22.1553586995.1553584904.',
    }
    base_url1 = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start={}&limit=20"  # 100-90的影片
    base_url2 = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=90%3A80&action=&start={}&limit=20"
    base_url3 = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=80%3A70&action=&start={}&limit=20"  # 80-70的影片
    base_url4 = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=70%3A60&action=&start={}&limit=20"
    base_url5 = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=60%3A50&action=&start={}&limit=20"
    base_url6 = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=50%3A40&action=&start={}&limit=20"
    base_url7 = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=40%3A30&action=&start={}&limit=20"
    base_url8 = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=30%3A20&action=&start={}&limit=20"
    base_url9 = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=20%3A10&action=&start={}&limit=20"
    base_url10 = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=10%3A0&action=&start={}&limit=20"
    base_url = [base_url1, base_url2, base_url3, base_url4, base_url5, base_url6, base_url7, base_url8, base_url9,
                base_url10, ]
    # print(base_url)
    num = 0
    juqing_Movie = []
    while num <= 0:  # num从0 意味着一共20部电影,一般都是每个段位600多电影
        i = 0
        while i <= 9:
            url = base_url[i].format(num)  # 构造url
            i += 1
            print(url)
            response = requests.get(url, headers=headers)
            html_str = response.content.decode()
            # print("可以访问网页")
            print(html_str)  # 检验是否可访问网页

            html = etree.HTML(html_str)
            print(html)
            dict_juqing = json.loads(html_str)  # 先把对象转换为json才可以操作
            print(type(dict_juqing))  # 判断类型  list类型。每个list[]里面都是一个字典
            juqing_Movie = juqing_Movie + dict_juqing
            print(len(juqing_Movie))

            for juqing in dict_juqing:
                print(juqing, "\n")
            # 输出电影信息
            print("第", i, "轮爬虫")
        # print("前", num , "部剧情片")
        print("每个段位前", num + 20, "部剧情片完成")
        num += 20

    print("爬虫结束")
    # 获取到了每一个电影的字典

    j_num = 0

    print(len(juqing_Movie))
    url_dict_juqing = []
    title_dict_juqing = []
    # print(type(juqing_Movie[2]))
    while j_num < len(juqing_Movie):
        dict = juqing_Movie[j_num]
        # url_dict_juqing[j_num]=dict['url']
        j_num += 1
        url_dict_juqing.append(dict['url'])
        title_dict_juqing.append(dict['title'])
        # print(dict['url'])
        print(url_dict_juqing)
        # 打印url地址
        # print(title_dict_juqing)
    # .........................................................

    # def get_juqing_info():
    #     i_num=0
    #     while i_num<len(url_dict_juqing)
    #         headers = {
    #             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    #             'Referer': 'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action=',
    #
    #             'Cookie': 'bid=YTmCMpU7VFw; gr_user_id=e89f7f05-54dd-48b7-b016-1cbd195fef72; _vwo_uuid_v2=DD062FA23089F729B3D9D0279EE32C888|f8d13e41707d3b501e94e849c4eac737; ct=y; viewed="25963163"; ll="118090"; __yadk_uid=rfKjYEj2QgfuQ9hJljPMqjKQqNsBfvhS; douban-fav-remind=1; dbcl2="154361022:9D3tjbsTYkM"; push_noty_num=0; push_doumail_num=0; __utmv=30149280.15436; __utmz=30149280.1553344867.9.6.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=223695111.1553402455.9.6.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ck=khHp; __utmc=30149280; __utmc=223695111; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1553586985%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.78084383.1551104327.1553584746.1553586986.22; __utmb=30149280.0.10.1553586986; __utma=223695111.759236850.1551332018.1553584746.1553586986.20; __utmb=223695111.0.10.1553586986; _pk_id.100001.4cf6=e70bd7ef5bb896fe.1551332017.22.1553586995.1553584904.',
    #         }
    #         get_info_url = url_dict_juqing[i_num]
    #         print(get_info_url)
    # 打印电影名称
    # 存入CSV
    # test = pd.DataFrame({'url地址': url_dict_juqing, '电影名': title_dict_juqing})
    # test.to_csv("juqing.csv", index=False, sep=',')
    return url_dict_juqing


if __name__ == "__main__":
    get_juqing_url_list()
