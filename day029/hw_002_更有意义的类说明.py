# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 08:39
# 文件名称: hw_002_更有意义的类说明.py
# 开发工具: PyCharm

class Person:
    def __init__(self, name='', age=0):
        self.__name = name
        self.__age = age

    def __str__(self):
        return "姓名:{}\n年龄:{}\n".format(
            self.__name, self.__age
        )


print(Person)
p = Person("张宝富", 33)
print(p)
