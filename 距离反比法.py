# -*- codeing =utf-8 -*-
# @Time : 2023/4/4$ 19:50
# Author : YantaoXI
# @File : 距离反比法.py
# @Software: PyCharm
import numpy as np

# 已知点的坐标和函数值
x_known = np.array([1, 2, 3, 4, 5])
y_known = np.array([0.5, 1.3, 3.1, 4.5, 5.0])
z_known = np.array([0.2, 0.8, 1.0, 2.1, 2.5])

# 待插值点的坐标
x_interp = np.array([1.5, 2.5, 3.5, 4.5])

# 设置距离反比法的参数
p = 2  # 距离反比法中的幂次参数

# 计算待插值点与已知点之间的距离
d = np.sqrt((x_known[:, None] - x_interp)**2)

# 计算距离的倒数的幂次
w = 1 / d**p

# 根据距离反比法计算插值结果
z_interp = np.sum(w * z_known[:, None], axis=0) / np.sum(w, axis=0)

# 输出插值结果
print(z_interp)
