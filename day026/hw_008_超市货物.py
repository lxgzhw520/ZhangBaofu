# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 06:49
# 文件名称: hw_008_超市货物.py
# 开发工具: PyCharm

class Goods:
    discount = 0.5  # 折扣

    def __init__(self, name, price):
        self.name = name
        self.__price = price

    # 需要打折
    # 折扣后的价格
    @property
    def price(self):
        return self.__price * Goods.discount


apple = Goods('苹果手机', 8999)
print(apple.price)

# 修改折扣
Goods.discount = 0.8
print(apple.price)
