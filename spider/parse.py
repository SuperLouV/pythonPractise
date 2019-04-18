import requests
from retrying import retry




# headers = {
#     'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
# # 'Referer': 'https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85%E7%89%87&type=11&interval_id=100:90&action=',
#         }
headers = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        'Referer': 'https://movie.douban.com/tag/',
    }
@retry(stop_max_attempt_number=3)
def _parse_url(url):
    print("*"*100)
    response = requests.get(url, headers=headers, timeout=5)
    return response.content.decode()

def parse_url(url):
    try:
        html_str = _parse_url(url)
    except:
        html_str = None
    return html_str
if __name__ == '__main__':
    url='https://www.baidu.com'
    print(parse_url(url))