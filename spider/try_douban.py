import json
import requests
url = "https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0"
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'Cookie': 'bid=YTmCMpU7VFw; gr_user_id=e89f7f05-54dd-48b7-b016-1cbd195fef72; _vwo_uuid_v2=DD062FA23089F729B3D9D0279EE32C888|f8d13e41707d3b501e94e849c4eac737; ct=y; viewed="25963163"; ll="118090"; __yadk_uid=rfKjYEj2QgfuQ9hJljPMqjKQqNsBfvhS; douban-fav-remind=1; __utmc=30149280; __utmz=30149280.1553058098.4.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ap_v=0,6.0; __utma=30149280.78084383.1551104327.1553058098.1553157103.5; __utmt=1; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1553157129%2C%22https%3A%2F%2Fwww.douban.com%2Fsearch%3Fq%3D%25E7%2594%25B5%25E8%25A7%2586%22%5D; _pk_ses.100001.4cf6=*; __utma=223695111.759236850.1551332018.1552284540.1553157129.3; __utmb=223695111.0.10.1553157129; __utmc=223695111; __utmz=223695111.1553157129.3.3.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/search; loc-last-index-location-id="118090"; __utmb=30149280.4.10.1553157103; _pk_id.100001.4cf6=e70bd7ef5bb896fe.1551332017.5.1553157282.1552284753.',
    # 'Referer': 'https://movie.douban.com/tv/',
        }
response = requests.get(url, headers=headers)
json_str = response.content.decode()
print(type(json_str))
ret1 = json.loads(json_str)
print(ret1)
with open("douban.txt","w",encoding="utf-8") as f:
    f.write(json.dumps(ret1,ensure_ascii=False,indent=2))