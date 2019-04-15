# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 07:48
# 文件名称: hw_005_多继承.py
# 开发工具: PyCharm

class FlyAnimal:
    def fly(self):
        print('会飞的动物')


class SwimAnimal:
    def swim(self):
        print("会游泳的动物")


class WalkAnimal:
    def walk(self):
        print("会走路的动物")


class Pandas(SwimAnimal, WalkAnimal):
    pass


p = Pandas()
p.walk()
p.swim()
