# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 06:46
# 文件名称: hw_008_随机数组的生成方法.py
# 开发工具: PyCharm
# randint(开始值,结束值) 用于生成随机整数
from random import randint

# 随机生成1-100之间的随机整数
l = [randint(1, 100) for i in range(100)]
print(l)

# 随机生成-100,100之间的随机整数
print([randint(-100, 100) for i in range(100)])
