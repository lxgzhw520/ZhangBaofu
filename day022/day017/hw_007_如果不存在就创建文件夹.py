# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 10:27
# 文件名称: hw_007_如果不存在就创建文件夹.py
# 开发工具: PyCharm

import os

if not os.path.exists('test'):
    os.mkdir('test')
