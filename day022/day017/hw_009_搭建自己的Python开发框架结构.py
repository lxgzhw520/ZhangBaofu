# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 10:30
# 文件名称: hw_009_搭建自己的Python开发框架结构.py
# 开发工具: PyCharm

"""
Python框架结构都是从创建文件夹开始的
需求:创建如下结构的框架
说明:带---是文件夹,不带的是文件
---lxgPyWeb
    main.py
    --- static
    --- templates
    --- apps
"""

# 分析
"""
1 创建文件夹lxgPyWeb  mkdir
2 进入lxgPyWeb chdir
3 创建文件 main.py 
4 创建文件夹static
5 创建文件夹templates
6 创建文件夹apps

"""
import os

if not os.path.exists('lxgPyWeb'):
    os.mkdir('lxgPyWeb')
os.chdir('lxgPyWeb')
with open('main.py', 'w', encoding='utf8') as f:
    f.write("# 作者:理想国真恵玩")
try:
    os.mkdir('static')
    os.mkdir('templates')
    os.mkdir('apps')
except Exception as e:
    pass

print("恭喜您,项目创建成功")
