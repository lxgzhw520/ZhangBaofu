# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 08:18
# 文件名称: Person.py
# 开发工具: PyCharm

class Person:
    b = '类属性测试'

    def __init__(self):
        self.name = '属性测试'

    @classmethod
    def a(cls):
        print("类方法测试")
