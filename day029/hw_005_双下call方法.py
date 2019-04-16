# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 08:58
# 文件名称: hw_005_双下call方法.py
# 开发工具: PyCharm


class A:
    def __call__(self, *args, **kwargs):
        print('实例被以函数方式执行的时候调用')


a = A()
# 以函数的方式执行
a()
#主动调用的时候也会执行
a.__call__()
