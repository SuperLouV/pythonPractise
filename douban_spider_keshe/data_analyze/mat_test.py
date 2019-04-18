from matplotlib import  pyplot as plt
# x = range(2,26,2)
# y=[15,13,14,5,17,20,25,26,27,22,18,15]
import random
import matplotlib
plt.rcParams['font.sans-serif'] = ['SimHei']
x = range(0,120)
y = [random.randint(20,35) for i in range(120)]
#设置图片大学
plt.figure(figsize=(20,8),dpi=80)
#绘图
plt.plot(x,y)



#设置X刻度
_xtick_labels = ["10点{}分".format(i)for i in range(60)]
_xtick_labels += ["11点{}分".format(i)for i in range(60)]
print(_xtick_labels)
plt.xticks(list(x)[::3],_xtick_labels[::3],rotation=45)
#保存
plt.savefig("./test2.png")

#添加描述信息
plt.xlabel("时间")
plt.ylabel("温度")
plt.title("10-12点气温变化")

#显示图像
plt.show()