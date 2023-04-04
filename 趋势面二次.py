# -*- codeing =utf-8 -*-
# @Time : 2023/4/4$ 19:42
# Author : YantaoXI
# @File : 趋势面二次.py
# @Software: PyCharm
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# 读取数据
df = pd.read_excel('趋势面.xlsx', sheet_name='Sheet1', usecols=['x', 'y', 'z'])

# 提取x、y和z列
x = df['x'].values
y = df['y'].values
z = df['z'].values

# 构造A矩阵
A = np.vstack([x**2, y**2, x*y, x, y, np.ones(len(x))]).T

# 使用最小二乘法拟合二次趋势面模型
a, b, c, d, e, f = np.linalg.lstsq(A, z, rcond=None)[0]

# 创建3D坐标系
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制散点图
ax.scatter(x, y, z)

# 构造新的x、y网格
new_x = np.linspace(min(x), max(x), 50)
new_y = np.linspace(min(y), max(y), 50)
new_x, new_y = np.meshgrid(new_x, new_y)

# 计算对应的z值
new_z = a*new_x**2 + b*new_y**2 + c*new_x*new_y + d*new_x + e*new_y + f

# 绘制二次趋势面
surf = ax.plot_surface(new_x, new_y, new_z, cmap='jet')

# 设置坐标轴标签
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# 设置图例
fig.colorbar(surf, shrink=0.5, aspect=5)

# 显示图形
plt.show()
