# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 21:16
# 文件名称: hw_008_静态方法.py
# 开发工具: PyCharm

# 静态方法就是不需要任何参数的方法
class Person:
    name = '人类'

    @staticmethod
    def show():
        print("静态方法也有自己的装饰器")
        # print(name) #静态方法不能调用类的属性


# 静态方法也可以直接调用
Person.show()
