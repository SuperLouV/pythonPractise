from webbrowser import Mozilla

import requests
url = "https://www.zhihu.com/"
headers = {
   'headers': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36',
    'Cookie': 'zap=7fc2cb22-ae70-4416-a0fa-cfe80f93a4a1; d_c0="AOBjXXxr5w6PToMMv-5U7tIQG_JpQ-CL4UQ=|1548828492"; q_c1=b892562242494dfb972b34a807575243|1548828494000|1548828494000; tgw_l7_route=4860b599c6644634a0abcd4d10d37251; _xsrf=pHGxyTwROKbT2iGhU4tT8BVaWJ0MWexc; capsion_ticket="2|1:0|10:1553152421|14:capsion_ticket|44:NzQ0ZWY1NTMyMTUxNGE2MzlmY2ZjODI3YTAwYmNlZDA=|f201efe516beb1081419dc0f3caa81db006b22ad72eab64d7bfdc22686a2c34f"; z_c0="2|1:0|10:1553152428|4:z_c0|92:Mi4xc3NpYUFnQUFBQUFBNEdOZGZHdm5EaVlBQUFCZ0FsVk5ySWVBWFFBZXZ5ZFRZU0VBaEs3c3dmS3pSUHpKalU0U0V3|2ee19ffca3c5be5138d79c712f58bccc432ab53f8c57cc82719204ca01d08d98"'
            }
response = requests.get(url,headers=headers,)
with open("zhihu1.html","w",encoding="utf-8") as f:
    f.write(response.content.decode())