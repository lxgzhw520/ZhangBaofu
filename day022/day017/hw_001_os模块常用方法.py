# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 10:06
# 文件名称: hw_001_os模块常用方法.py
# 开发工具: PyCharm

import os

# 打印当前所在绝对路径
print(os.getcwd())
# 切换文件夹
os.chdir('..')
print(os.getcwd())

os.chdir('day017')
print(os.getcwd())
# 查看文件夹
print(os.listdir('.'))
# 同时创建多级文件夹
# 判断文件夹是否存在
if os._exists('test01/test01/test01'):
    os.makedirs('test01/test01/test01')
    os.removedirs('test01')
print(os.listdir('.'))
# 删除文件夹
# os.remove('test01')
print(os.listdir('.'))
