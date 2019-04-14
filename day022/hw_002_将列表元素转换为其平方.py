# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 06:59
# 文件名称: hw_002_将列表元素转换为其平方.py
# 开发工具: PyCharm

# 需求:将列表元素转换为其平方
# 思路:和上一个一样

# 1 生成随机数的列表
from random import randint

l = [randint(-100, 100) for i in range(10)]
# 2 用map(匿名函数,列表)
ret = map(lambda x: x ** 2, l)
# 3 将执行结果转换为列表并打印
print(list(ret))
# 4 用一行代码解决
print(list(map(lambda x: x ** 2, [randint(-100, 100) for i in range(10)])))
