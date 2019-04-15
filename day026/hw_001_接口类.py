# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 22:03
# 文件名称: hw_001_接口类.py
# 开发工具: PyCharm

from abc import abstractmethod, ABCMeta


# 定义一个接口
# 子类要继承接口就必须实现接口的方法
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money): pass


class Wechat(Payment):
    def pay(self, money):
        print("微信支付:{}".format(money))


class Alipay(Payment):
    def pay(self, money):
        print("支付宝支付:{}".format(money))


class Apppay(Payment):
    def pay(self, money):
        print("手机商城支付:{}".format(money))


def pay(obj, money):
    obj.pay(money)


wechat = Wechat()
pay(wechat, 33)
