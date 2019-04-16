# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-17 07:02
# 文件名称: hw_008_函数复习.py
# 开发工具: PyCharm
def f(a, b=3, *args, **kwargs):
    print(a)
    print(b)
    for i in args:
        print(i, end='')
    for i in kwargs.items():
        print(i)


f(1, 333, 12, 123, 123, aa=333, bb=666)
f(1, 333, 12, 123, 123, aa=333, bb=666, cc=999, dd=000)
