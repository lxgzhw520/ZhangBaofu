# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 06:35
# 文件名称: hw_005_父类私有属性.py
# 开发工具: PyCharm

# 子类能使用父类的私有属性吗
class Person:
    __name = '人类'


class Student(Person):
    def show(self):
        print(self.__name)


s = Student()
# 子类不能使用父类的私有属性
s.show()
