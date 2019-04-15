# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 06:52
# 文件名称: hw_009_属性的增删改查.py
# 开发工具: PyCharm

class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    # 用装饰器删除
    @name.deleter
    def name(self):
        print("删除{}成功.".format(self.name))
        del self.__name

    # 修改方法
    @name.setter
    def name(self, new_name):
        print("习惯{}为{}成功.".format(self.name, new_name))
        self.__name = new_name


zbf = Person('张宝富')
print(zbf.name)
# 修改
zbf.name = '张宝富-修改'
print(zbf.name)
del zbf.name
# 删除以后,属性不存在
# print(zbf.name)
