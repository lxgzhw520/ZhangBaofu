# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 06:48
# 文件名称: hw_009_filter的进阶用法.py
# 开发工具: PyCharm


# 生成一个随机数组,用filter获取其中的偶数

from random import randint

l = [randint(-100, 100) for i in range(100)]

print(filter(lambda x: x % 2 == 0, l))
# 转换为列表后打印
print(list(filter(lambda x: x % 2 == 0, l)))
# 直接遍历打印
for i in filter(lambda x: x % 2 == 0, l):
    print(i, end='\t')
