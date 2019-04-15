# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 22:08
# 文件名称: hw_002_接口类的多继承.py
# 开发工具: PyCharm

# 动物 有会飞的 会游泳的,会走路的
from abc import abstractmethod, ABCMeta


class FlyAnimal(metaclass=ABCMeta):
    @abstractmethod
    def fly(self): pass


class WalkAnimal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self): pass


class SwimAnimal(metaclass=ABCMeta):
    @abstractmethod
    def swim(self): pass


# 鳄鱼
class Cayman(WalkAnimal, SwimAnimal):
    def walk(self):
        print("鳄鱼会走路")

    def swim(self):
        print("鳄鱼会游泳")


c = Cayman()
c.walk()
c.swim()
