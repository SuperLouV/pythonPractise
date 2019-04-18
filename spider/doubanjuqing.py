import json
import requests
url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20"
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'Referer': 'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85%E7%89%87&type=11&interval_id=100:90&action=',
        }
response = requests.get(url, headers=headers)
json_str = response.content.decode()
print(type(json_str))
ret1 = json.loads(json_str)
print(ret1)
# with open("juqing.txt","w",encoding="utf-8") as f:
#     f.write(json.dumps(ret1,ensure_ascii=False,indent=2))