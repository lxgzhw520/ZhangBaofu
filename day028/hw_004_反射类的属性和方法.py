# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 08:14
# 文件名称: hw_004_反射类的属性和方法.py
# 开发工具: PyCharm

class A:
    @classmethod
    def a(cls):
        print('类方法测试')

    @staticmethod
    def b():
        print('静态方法测试')

    @property
    def name(self):
        print("属性方法测试")


a = A()
# 反射类的属性和方法
getattr(a, 'a')()
getattr(a, 'b')()
getattr(a, 'name')

# 判断是否能够反射
print(hasattr(a, 'a'))
print(hasattr(a, 'b'))
print(hasattr(a, 'name'))
