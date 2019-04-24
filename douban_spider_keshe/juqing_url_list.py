import json

import pandas as pd
from lxml import etree
import requests
from douban_spider_keshe.juqing import get_juqing_url_list

for final_url in get_juqing_url_list():
    # print(final_url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'Referer': 'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action=',

        'Cookie': 'bid=YTmCMpU7VFw; gr_user_id=e89f7f05-54dd-48b7-b016-1cbd195fef72; _vwo_uuid_v2=DD062FA23089F729B3D9D0279EE32C888|f8d13e41707d3b501e94e849c4eac737; ct=y; viewed="25963163"; ll="118090"; __yadk_uid=rfKjYEj2QgfuQ9hJljPMqjKQqNsBfvhS; douban-fav-remind=1; dbcl2="154361022:9D3tjbsTYkM"; push_noty_num=0; push_doumail_num=0; __utmv=30149280.15436; __utmz=30149280.1553344867.9.6.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=223695111.1553402455.9.6.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ck=khHp; __utmc=30149280; __utmc=223695111; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1553586985%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.78084383.1551104327.1553584746.1553586986.22; __utmb=30149280.0.10.1553586986; __utma=223695111.759236850.1551332018.1553584746.1553586986.20; __utmb=223695111.0.10.1553586986; _pk_id.100001.4cf6=e70bd7ef5bb896fe.1551332017.22.1553586995.1553584904.',
    }
    response = requests.get(final_url, headers=headers)
    html_str = response.content.decode()
    # print("可以访问网页")
    # print(html_str)              # 检验是否可访问网页
    html = etree.HTML(html_str)
    # juqing_info = html.xpath('/html//div[@class="info"]/span/a')
    juqing_director = html.xpath('//span[@class="attrs"]/a[1]/text()')
    juqing_director_director = juqing_director[0]
    juqing_director_screenwriter = juqing_director[1]
    # // span[ @ property = "v:genre"]
    print("-" * 50)
    print(type(juqing_director))
    # print(len(juqing_info))
    print(juqing_director)
    print("导演为:", juqing_director_director)
    print("编剧为：", juqing_director_screenwriter)

    # a=json.loads(juqing_info[0])
    # print("数组内存储形式为：",type(a))
    # print(type(a))
    # 检验获取到了juqing的第二段链接info对象
    # final_juqing = json.loads(juqing_info)
    # print(final_url)
