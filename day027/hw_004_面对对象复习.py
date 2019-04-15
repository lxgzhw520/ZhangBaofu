# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 07:41
# 文件名称: hw_004_面对对象复习.py
# 开发工具: PyCharm

# 定义
class Person:
    name = '人类'

    @classmethod
    def show(cls):
        print(cls.name)


# 继承
class Student(Person):
    name = '学生'

    @classmethod
    def show(cls):
        # 使用父类的方法
        Person.show()
        print(cls.name)


# 实例化
zbf = Student()
zbf.show()
