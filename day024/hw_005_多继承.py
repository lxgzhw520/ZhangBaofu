# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 21:00
# 文件名称: hw_005_多继承.py
# 开发工具: PyCharm

class Person:
    __name = '人类'

    def show(self):
        print(self.__name)


class Student:
    __name = '学生'

    def show(self):
        print(self.__name)


# 多继承只需要在括号里多写几个要继承的父类即可
class Me(Person, Student):
    __name = '我就是我'

    def show(self):
        Person.show(self)
        Student.show(self)
        print(self.__name)


lky = Me()
lky.show()
