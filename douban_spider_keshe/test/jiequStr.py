def cut_str(strs):
    # strs = ['asdads', 'fdsgf', 'ds/h', 's/yj/u', 'asd/hgf', 'ad/b/gf']
    # strs = ['asdads', 'fdsgf', 'ds/h', 's/yj/u', 'asd/hgf', 'ds/h', 's/yj/u', 'asd/hgf']
    # n=random.randint(0,len(strs))
    # print(strs[n])#返回一个字符串数组随机位置的字符串
    i = 0
    sign='/'
    for str in strs:
        if sign in str:
            location = strs[i].index('/')
            strs[i] = str[0:location]
            i += 1
        else:
            i+=1
    print(strs)
if __name__=="__main__":
    cut_str()