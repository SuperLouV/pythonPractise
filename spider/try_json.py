import json

import requests
url = "https://fanyi.baidu.com/transapi"
query_str = input("请输入要翻译的中文：")

data = {'query': query_str,
        'from': 'zh',
        'to': 'en',
        }
headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
            # "Referer": "https://fanyi.baidu.com/"
            }
response = requests.post(url,data=data,headers=headers)

html_str = response.content.decode()
dict_ret = json.loads(html_str)
# print(dict_ret)
# print(type(dict_ret))
ret = dict_ret["data"][0]["dst"]  #data对应的是一个列表 列表的第一个元素时所要结果， 然后取dst对应的就是hello
print("翻译结果是：",ret)