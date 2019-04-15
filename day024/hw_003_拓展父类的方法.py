# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 20:52
# 文件名称: hw_003_拓展父类的方法.py
# 开发工具: PyCharm

# 如果我们想要使用父类的方法,但是又想要自己定义新的内容
# 拓展

class Person:
    def __init__(self):
        pass

    def show(self):
        print("我是一个人类")


class Student(Person):
    def show(self):
        Person.show(self)
        print("我是一个学生")


lky = Student()
# 能够同时使用父类的方法
# 也有自己的方法
lky.show()
