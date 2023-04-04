# -*- codeing =utf-8 -*-
# @Time : 2023/4/4$ 11:27
# Author : YantaoXI
# @File : 一元数据描述.py
# @Software: PyCharm
import pandas as pd
import scipy.stats as stats
import statistics
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['font.sans-serif'] =['SimHei']
mpl.rcParams['font.serif'] =['SimHei']
mpl.rcParams['axes.unicode_minus'] =False# 解决保存图像是负号'-'显示为方块的问题,或者转换负号为字符串
# 读取Excel文件
df = pd.read_excel(r'D:\Geo_Data\data\geodata.xlsx', sheet_name='data', header=0)

# 指定列名称
col_name = '品位'

# 计算频率分布
hist, bins = np.histogram(df[col_name], bins=10)

# 绘制频率分布图
plt.hist(df[col_name], bins=20, color='skyblue')
plt.xlabel(col_name)
plt.ylabel('Frequency')
plt.title('Histogram of ' + col_name)
plt.show()

# 计算算术平均值
mean = df[col_name].mean()

# 计算加权平均值（需要提供权重列）
w_col_name = '权重'
wmean = (df[col_name] * df[w_col_name]).sum() / df[w_col_name].sum()

# 计算几何平均值
gmean = stats.gmean(df[col_name])

# 计算中位数
median = df[col_name].median()

# 计算众数
mode = statistics.mode(df[col_name])

# 输出结果
print(f"算术平均值：{mean:.2f}")
print(f"加权平均值：{wmean:.2f}")
print(f"几何平均值：{gmean:.2f}")
print(f"中位数：{median:.2f}")
print(f"众数：{mode:.2f}")

# 计算极差
range = np.max(df[col_name]) - np.min(df[col_name])

# 计算方差
variance = np.var(df[col_name])

# 计算标准差
std_deviation = np.std(df[col_name])

# 计算变异系数
coefficient_of_variation = std_deviation / np.mean(df[col_name]) * 100

# 输出结果
print('极差：', range)
print('方差：', variance)
print('标准差：', std_deviation)
print('变异系数：', coefficient_of_variation)


# 计算百分位数
pct_25 = np.percentile(df[col_name], 25)
pct_50 = np.percentile(df[col_name], 50)
pct_75 = np.percentile(df[col_name], 75)

# 绘制盒须图
plt.boxplot(df[col_name], notch=True, vert=False, widths=0.5, whis=1.5, labels=[col_name])
plt.scatter([pct_25, pct_50, pct_75], [1, 1, 1], c='r', marker='o')
plt.xlabel(col_name)
plt.title('Boxplot of ' + col_name)
plt.show()

# 计算指定列的峰度和偏度
kurtosis = stats.kurtosis(df[col_name], nan_policy='omit')
skewness = stats.skew(df[col_name], nan_policy='omit')

# 输出结果
print('峰度:', kurtosis)
print('偏度:', skewness)

# kurtosis 表示指定列的峰度（kurtosis），
# 是统计学中衡量数据分布形态陡峭程度的指标，通常与正态分布相比较，正态分布的峰度为 0。
# 当峰度大于 0 时，说明数据分布比正态分布更加陡峭，峰顶更加尖锐；
# 当峰度小于 0 时，说明数据分布比正态分布更加平缓，峰顶更加平缓。
#
# skewness 表示指定列的偏度（skewness），是统计学中衡量数据分布的偏斜程度的指标，
# 通常与对称分布相比较，对称分布的偏度为 0。
# 当偏度大于 0 时，说明数据分布偏向左侧（负偏），即左侧的尾巴比右侧的尾巴长；当
# 偏度小于 0 时，说明数据分布偏向右侧（正偏），即右侧的尾巴比左侧的尾巴长。