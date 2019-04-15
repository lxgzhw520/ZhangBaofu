# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 06:42
# 文件名称: hw_007_BMI指数.py
# 开发工具: PyCharm

class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    @property
    def bmi(self):
        """
        w = 體重，單位：公斤;
        h = 身高，單位：公尺;
        BMI = 身高體重指數，單位：公斤/平方公尺
        """
        return self.weight / (self.height ** 2)


zbf = Person('张宝富', 60, 1.88)
print(zbf.bmi)
