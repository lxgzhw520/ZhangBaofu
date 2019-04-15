# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 06:38
# 文件名称: hw_006_property.py
# 开发工具: PyCharm


from math import pi


# property 将方法转换为属性
class Circle:
    def __init__(self, r):
        self.r = r

    # 将方法转换为属性
    @property
    def perimeter(self):
        """周长"""
        return 2 * pi * self.r

    @property
    def area(self):
        """面积"""
        return self.r ** 2 * pi


c = Circle(33)
# 属性的特点,不需要在后面加括号
print(c.perimeter)
print(c.area)
