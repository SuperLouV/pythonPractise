import json

import self as self
from parse import parse_url

# from spider.try_json import html_str


class DoubanSpider:
    headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        'Referer': 'https://movie.douban.com/tag/',
    }

    def __init__(self):
        self.temp_url = "https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start={}&genres=%E5%89%A7%E6%83%85"

    def get_contentf_list(self,html_str):
        dict_data = json.loads(html_str)
        content_list = dict_data["data"]
        return  content_list

    def save_content_list(self,content_list):
        with open("douban.json","a",encoding="utf-8")as f:
            for content in content_list:
                f.write(json.dumps(content,ensure_ascii=False))
                f.write("\n")
    print("保存成功")

    def run(ok):#实现主要逻辑
        num = 0
        total = 500
        while num<total:
            url = ok.temp_url.format(num)
            print(url)
            html_str = parse_url(url)
            content_list = ok.get_contentf_list(html_str)
            ok.save_content_list(content_list)
            num = num + 80


# start url
# 发送请求，获取相应
# 提取数据
# 保存
# 构造下一页

if __name__ == '__main__':
    douban = DoubanSpider()
    douban.run()