# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 07:02
# 文件名称: hw_003_列表元素排序.py
# 开发工具: PyCharm

# 需求 hw_003_列表元素排序
# 生成随机数组
from random import randint

l = [randint(-100, 100) for i in range(20)]
print(l)
# 1 从小到大排序
l.sort()
print(l)
# 2 从大到小排序
l.sort(reverse=True)
print(l)
# 3 根据绝对值从小到大排序
l.sort(key=abs)
print(l)
