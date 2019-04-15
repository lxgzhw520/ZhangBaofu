# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 07:00
# 文件名称: hw_001_类方法.py
# 开发工具: PyCharm

"""
复习
method 方法
staticmethod 静态方法
classmethod 类方法
类的操作行为
"""


# 需求,封装折扣
class Goods:
    __discount = 0.5  # 折扣

    def __init__(self, name, price):
        self.name = name
        self.__price = price

    # 需要打折
    # 折扣后的价格
    @property
    def price(self):
        return self.__price * Goods.__discount

    # 类方法是通过类名进行操作
    # 这个装饰器把一个方法转换为类方法
    @classmethod
    def update_dicount(cls, new_discount):
        cls.__discount = new_discount


apple = Goods('苹果', 8)
print(apple.price)
Goods.update_dicount(0.8)
print(apple.price)
