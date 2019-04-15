# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 21:21
# 文件名称: hw_001_类的new方法.py
# 开发工具: PyCharm

class Person:
    def __new__(cls, *args, **kwargs):
        print("创建对象的时候会自动执行")


lky = Person()
