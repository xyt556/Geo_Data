# -*- codeing =utf-8 -*-
# @Time : 2023/4/4$ 17:19
# Author : YantaoXI
# @File : 趋势面.py
# @Software: PyCharm
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

df = pd.read_excel('趋势面.xlsx', usecols=['x', 'y', 'z'])

# 提取x、y和z列
x = df['x'].values
y = df['y'].values
z = df['z'].values

# 构造A矩阵
A = np.vstack([x, y, np.ones(len(x))]).T

# 使用最小二乘法拟合线性趋势面模型
m, n, c = np.linalg.lstsq(A, z, rcond=None)[0]

# 显示结果
print("一次趋势面方程为: z = {}x + {}y + {}".format(m, n, c))

# 生成网格点数据
xx, yy = np.meshgrid(np.linspace(x.min(), x.max(), 10), np.linspace(y.min(), y.max(), 10))
zz = m * xx + n * yy + c

# 绘制3D图像
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(xx, yy, zz, rstride=1, cstride=1, cmap='jet', alpha=0.8)
ax.scatter(x, y, z, c='black', s=30)
plt.show()
