import random
import random

strs=['asd/ads','fds/gf','ds/h','s/yju','asd/hgf','ad/bgf']
# n=random.randint(0,len(strs))
# print(strs[n])#返回一个字符串数组随机位置的字符串
print(strs[1])
i=0
for str in strs:
    location=strs[i].index('/')
    print(strs[i].index('/'))
    strs[i]=str[0:location]
    i+=1
print(strs)


