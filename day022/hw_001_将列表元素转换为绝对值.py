# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 06:55
# 文件名称: hw_001_将列表元素转换为绝对值.py
# 开发工具: PyCharm


# 需求:将列表中的每一个元素转换为其绝对值
# 生成一个-100 - 100 直接的随机列表

from random import randint

l = [randint(-100, 100) for i in range(10)]
print(l)

# 分析:使用map函数
# 1 用map函数(匿名函数,列表) 将列表中的每一个元素映射为绝对值
ret = map(lambda x: abs(x), l)
# 2 将map函数处理后的结果转换为列表打印
print(list(ret))

# 用一行代码解决
print(list(map(lambda x: abs(x), [randint(-100, 100) for i in range(10)])))
