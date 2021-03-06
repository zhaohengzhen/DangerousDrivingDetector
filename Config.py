# encoding: utf-8

"""
@version: 2.0
@author: Aristochi & Dohaeris
@software: PyCharm
@file: Config.py
@time: 2020/1/20 23:14
"""

import os.path as osp
sk = [ 15, 30, 60, 111, 162, 213, 264 ]
feature_map = [ 38, 19, 10, 5, 3, 1 ]
steps = [ 8, 16, 32, 64, 100, 300 ]
image_size = 300
aspect_ratios = [[2], [2, 3], [2, 3], [2, 3], [2], [2]]
MEANS = (104, 117, 123)
batch_size = 4
data_load_number_worker = 0
lr = 5e-4
momentum = 0.9
weight_decacy = 5e-4
gamma = 0.1
VOC_ROOT = osp.join('./', "dataset/")
dataset_root = VOC_ROOT
use_cuda = True
# lr_steps = (80000, 100000, 120000)
lr_steps = (8000, 10000, 12000)
max_iter = 120000
class_num = 7
class_num2= 7