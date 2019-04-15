# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 21:04
# 文件名称: hw_006_类属性和类方法.py
# 开发工具: PyCharm

class Person:
    name = '人类'  # 类属性

    # 用装饰器装饰  参数是cls的是类方法
    @classmethod
    def show(cls):
        print(cls.name)


# 类方法可以不实例化直接调用
Person.show()
