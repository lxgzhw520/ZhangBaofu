# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/4/3 21:18
# 文件名称: hw_001_创建元组.py
# 开发工具: PyCharm

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"

# 什么是元组
# 序列

# 怎么定义
# 1 空元组
t = ()
print(type(t))
# <class 'tuple'>

t1 = tuple()
print(type(t1))

# 定义只有一个元素元组
print(type((1,)))
# 类型转换
print(type(tuple([1])))

# 多个数
# 原理:都是元组 可以一一对应
a, b = 3, 5
print(a)
print(b)
# 有什么特点
# 不可修改  其他情况 一般都可以用列表

