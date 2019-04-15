# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 07:51
# 文件名称: hw_006_封装.py
# 开发工具: PyCharm

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age


zbf = Person("张宝富", 33)
print(zbf.name)
print(zbf.age)
