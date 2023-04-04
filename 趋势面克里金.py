# -*- codeing =utf-8 -*-
# @Time : 2023/4/4$ 19:48
# Author : YantaoXI
# @File : 趋势面克里金.py
# @Software: PyCharm
import pandas as pd
import numpy as np
from scipy.spatial.distance import cdist

# 读取数据
df = pd.read_excel('趋势面.xlsx', sheet_name='Sheet1', usecols=['x', 'y', 'z'])

# 选定插值点的坐标
xi = np.linspace(df['x'].min(), df['x'].max(), 50)
yi = np.linspace(df['y'].min(), df['y'].max(), 50)
xi, yi = np.meshgrid(xi, yi)
xi, yi = xi.flatten(), yi.flatten()

# 定义半方差函数
def k(h, a, c):
    return c**2 * (1.5*h/a - 0.5*(h/a)**3)

# 拟合克里金模型
a, c = 10, 1
K = k(cdist(df[['x', 'y']], df[['x', 'y']]), a, c)
w = np.linalg.solve(K, df['z'])
Kx = k(cdist(df[['x', 'y']], np.column_stack((xi, yi))), a, c)
zi = np.dot(Kx.T, w)

# 绘制结果
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(df['x'], df['y'], df['z'], c='r', marker='o')
ax.plot_trisurf(xi, yi, zi, cmap='jet', edgecolor='none', alpha=0.5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
