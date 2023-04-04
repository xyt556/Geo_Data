# -*- codeing =utf-8 -*-
# @Time : 2023/4/4$ 17:19
# Author : YantaoXI
# @File : 趋势面.py
# @Software: PyCharm
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# 读取Excel文件，指定工作表和列
df = pd.read_excel('rD:\Geo_Data\趋势面.xlsx', sheet_name='Sheet1', usecols=['x', 'y', 'z'])
print(df)

# 添加一列全为1的常数列
df['const'] = 1

# 构造设计矩阵X和响应变量向量Y
X = df[['x', 'y', 'const']]
Y = df['z']

# 求解线性回归系数
beta = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(Y)

# 构造平面方程
xx, yy = np.meshgrid(np.linspace(df['x'].min(), df['x'].max(), 100),
                     np.linspace(df['y'].min(), df['y'].max(), 100))
zz = beta[0]*xx + beta[1]*yy + beta[2]

# 绘制3D趋势面图
fig = plt.figure()
ax = Axes3D(fig)
surf = ax.plot_surface(xx, yy, zz, cmap='jet')
fig.colorbar(surf, shrink=0.5, aspect=5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
