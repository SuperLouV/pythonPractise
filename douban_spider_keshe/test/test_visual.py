import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def age_Dis():  # 统计年龄分布
    pr = pd.read_csv("hydata_swjl_0.csv")
    pr1 = pd.read_csv("hydata_swjl_1.csv", low_memory=False)
    print("统计年龄分布：")
    print()
    age = []
    for i in pr['BIRTHDAY']:
        age.append(int((20181219 - i) / 10000))
    print(age)
    age1 = []
    age2 = []
    age3 = []
    age4 = []
    age5 = []
    for i in age:
        if 18 <= i < 25:
            age1.append(i)
        elif 25 <= i < 35:
            age2.append(i)
        elif 35 <= i < 45:
            age3.append(i)
        elif 45 <= i < 55:
            age4.append(i)
        else:
            age5.append(i)

    index = ['18~25', '25~35', '35~45', '45~55', 'others']
    values = [len(age1), len(age2), len(age3), len(age4), len(age5)]
    plt.bar(index, values)
    plt.show()


if __name__ == "__main__":
    age_Dis()
