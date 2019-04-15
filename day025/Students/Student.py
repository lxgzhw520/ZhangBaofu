# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 21:38
# 文件名称: Student.py
# 开发工具: PyCharm
class Student:
    name = '学生'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("姓名:{}\n年龄:{}\n".format(
            self.name, self.age
        ))

    @classmethod
    def class_method(cls):
        print(cls.name)

    @staticmethod
    def static_method():
        print('类的静态方法')
