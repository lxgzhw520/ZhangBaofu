# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 10:18
# 文件名称: hw_004_判断文件夹是否存在.py
# 开发工具: PyCharm

import os

# print(os._exists('test'))
print(os.path.exists('test'))
print(os.path.exists('test/test'))
print(os.path.exists('test/test/test'))
print(os.path.exists('test/test/test/test'))
