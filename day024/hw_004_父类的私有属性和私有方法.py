# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 20:56
# 文件名称: hw_004_父类的私有属性和私有方法.py
# 开发工具: PyCharm

class Person:
    # 这种在前面加__的变量是私有属性,外部无法直接访问
    __name = '人类'

    # 这种在前面加__的是私有方法,外部无法直接访问
    def __test(self):
        print('这是不想被子类直接访问的方法')

    def show(self):
        print('我是人类')
        # 私有属性和私有方法可以通过公共方法暴露给外部
        self.__test()
        print("父类的私有属性:", self.__name)


class Student(Person):
    def show(self):
        Person.show(self)
        print("我是学生")


lky = Student()
lky.show()
