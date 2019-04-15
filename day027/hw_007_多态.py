# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 07:53
# 文件名称: hw_007_多态.py
# 开发工具: PyCharm

class Person:
    def __init__(self, name='', age=0):
        self.name = name
        self.age = age

    def show(self):
        print("人类")


# 多态,继承同一个类,但是表现形式却多种多样
class Student(Person):
    def show(self):
        print("学生")


class Father(Person):
    def show(self):
        print('父亲')


class Teacher(Person):
    def show(self):
        print('老师')


zbf = Student("张宝富", 33)
zbf.show()
p = Person()
p.show()
f = Father()
f.show()
t = Teacher()
t.show()
