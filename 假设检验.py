# -*- codeing =utf-8 -*-
# @Time : 2023/4/4$ 13:44
# Author : YantaoXI
# @File : 假设检验.py
# @Software: PyCharm
from scipy import stats
import numpy as np

# 假设有一组样本数据
data = np.array([4.9, 5.1, 4.8, 5.2, 4.7, 5.3, 4.6, 5.4, 4.5, 5.5])
print(f"mean={data.mean():.2f}")
# 假设检验
mu = 5
alpha = 0.05
t, p = stats.ttest_1samp(data, mu)
print(f"t={t:.2f}")
print(f"p={p:.2f}")
if p < alpha:
    print('拒绝原假设，样本的均值不等于5')
else:
    print('接受原假设，样本的均值等于5')
