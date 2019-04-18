import requests
url = "https://fanyi.baidu.com/transapi"
data = {'query': '你好',
        'from': 'zh',
        'to': 'en',

        }
headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
            # "Referer": "https://fanyi.baidu.com/"
            }
response = requests.post(url,data=data,headers=headers)
#print('231')
print(response)
response.encoding = "uts-8"
print(response.text)
print(response.content.decode())
print(type(response.content.decode()))
