# -*- codeing =utf-8 -*-
# @Time : 2023/4/4$ 19:43
# Author : YantaoXI
# @File : 趋势面三次.py
# @Software: PyCharm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# 读取数据
df = pd.read_excel('趋势面.xlsx', usecols=['x', 'y', 'z'])
x, y, z = df['x'].values, df['y'].values, df['z'].values

# 构造矩阵A和向量b
n = len(x)
A = np.zeros((n, 10))
A[:, 0] = 1
A[:, 1] = x
A[:, 2] = y
A[:, 3] = x * y
A[:, 4] = x ** 2
A[:, 5] = y ** 2
A[:, 6] = x ** 3
A[:, 7] = y ** 3
A[:, 8] = x ** 2 * y
A[:, 9] = x * y ** 2
b = z.reshape(n, 1)

# 求解最小二乘解
ATA = np.dot(A.T, A)
ATb = np.dot(A.T, b)
coeff = np.linalg.solve(ATA, ATb)

# 生成网格数据
X, Y = np.meshgrid(np.linspace(x.min(), x.max(), 100), np.linspace(y.min(), y.max(), 100))
Z = np.zeros((100, 100))
for i in range(100):
    for j in range(100):
        Z[i][j] = coeff[0] + coeff[1]*X[i][j] + coeff[2]*Y[i][j] + coeff[3]*X[i][j]*Y[i][j] \
                    + coeff[4]*X[i][j]**2 + coeff[5]*Y[i][j]**2 + coeff[6]*X[i][j]**3 \
                    + coeff[7]*Y[i][j]**3 + coeff[8]*X[i][j]**2*Y[i][j] + coeff[9]*X[i][j]*Y[i][j]**2

# 绘制图形
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()
