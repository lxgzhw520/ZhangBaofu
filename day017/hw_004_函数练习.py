# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-14 06:56
# 文件名称: hw_004_函数练习.py
# 开发工具: PyCharm

# 练习1: 定义一个函数 返回1-100的数之和
def add100():
    sum = 0
    for i in range(101):
        sum += i
    return sum


# 练习1: 定义一个函数 返回1-100的偶数之和
def add100_even():
    sum = 0
    for i in range(101):
        if i % 2 == 0:
            sum += i
    return sum


# 调用
print(add100())
print(add100_even())
