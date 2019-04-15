# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 10:21
# 文件名称: hw_005_判断文件夹是否为空.py
# 开发工具: PyCharm
import os

print(os.listdir('test'))
print(os.listdir('test/test'))
print(bool(os.listdir('test/test')))
print(bool(os.listdir('test/test/test')))
