# -*- codeing =utf-8 -*-
# @Time : 2023/4/4$ 10:52
# Author : YantaoXI
# @File : hist.py
# @Software: PyCharm
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] =['SimHei']
mpl.rcParams['font.serif'] =['SimHei']
mpl.rcParams['axes.unicode_minus'] =False# 解决保存图像是负号'-'显示为方块的问题,或者转换负号为字符串
# 生成随机数据
data = np.random.normal(size=1000)

# 设置直方图的边界和数量
bin_edges = np.arange(-4, 4.1, 0.2)

# 绘制直方图
plt.hist(data, bins=bin_edges, density=False, alpha=0.7, edgecolor='black')

# 设置标题和坐标轴标签
plt.title('直方图 of Random Data')
plt.xlabel('Value')
plt.ylabel('Frequency')

# 显示图形
plt.show()
