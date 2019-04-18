from lxml import etree
import requests

url = "https://movie.douban.com/chart"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',

}
response = requests.get(url,headers=headers)
html_str = response.content.decode()
# print(html_str)
html = etree.HTML(html_str)
# print(html)  #这是一个对象
url_list=html.xpath('//div[@class="indent"]/div/table//div[@class="pl2"]/a/@href')
# print(url_list)
#图片地址
image_url=html.xpath('//div[@class="indent"]/div/table//a[@class="nbg"]/img/@src')
# print(image_url)
#电影名称
name_list=html.xpath('//div[@class="indent"]/div/table//div[@class="pl2"]/a/text()')
# print(name_list)
ret1=html.xpath('//div[@class="indent"]/div/table')
print(ret1)

for table in ret1:
    item = {}
    item["title"] = table.xpath('.//div[@class="pl2"]/a/text()')[0].replace("/","").strip()  #电影名
    item["href"] = table.xpath('.//div[@class="pl2"]/a/@href')[0]#地址
    item["image"] = table.xpath('.//a[@class="nbg"]/img/@src')[0]#图片地址
    item["comment_num"]=table.xpath(".//span[@class='pl']/text()")[0]#评论数
    item["rating_num"] = table.xpath(".//span[@class='rating_nums']/text()")[0]  # 评论数
    # item["title"] = [for i in item["title"]]
    print(item)