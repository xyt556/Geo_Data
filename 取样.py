# -*- codeing =utf-8 -*-
# @Time : 2023/4/4$ 12:05
# Author : YantaoXI
# @File : 取样.py
# @Software: PyCharm
import pandas as pd
import numpy as np

# 读取 Excel 文件，选择指定的工作表和列
# 读取Excel文件
df = pd.read_excel(r'D:\Geo_Data\data\geodata.xlsx', sheet_name='data', header=0)

# 创建ExcelWriter对象，用于写入新的表格
with pd.ExcelWriter('sampled_file.xlsx', engine='openpyxl') as writer:

    # 对某一列进行多种抽样方法，分别写入不同的表格中
    sampled_data = df['品位']

    # 简单随机抽样
    simple_random_sample = df.sample(n=20)
    simple_random_sample_df = pd.DataFrame(simple_random_sample)
    simple_random_sample_df.to_excel(writer, sheet_name='随机抽样', index=False)

    # 分层抽样
    stratified_sample = df.groupby('stratum').apply(lambda x: x.sample(frac=0.1)) # 抽样比例0.5
    stratified_sample_df = pd.DataFrame(stratified_sample)
    stratified_sample_df.to_excel(writer, sheet_name='分层抽样', index=False)
    #
    # 系统抽样
    systematic_sample = df.iloc[::3] # 每隔3个数据取一个数据，形成系统抽样的样本数据
    systematic_sample_df = pd.DataFrame(systematic_sample)
    systematic_sample_df.to_excel(writer, sheet_name='系统抽样', index=False)

