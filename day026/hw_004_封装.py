# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 06:31
# 文件名称: hw_004_封装.py
# 开发工具: PyCharm


# 封装就是把具体细节隐藏,只暴露一个结果
class Room:
    def __init__(self, name, length, width):
        self.name = name
        self.__length = length
        self.__width = width

    def area(self):
        print("房屋主人:{}\n房屋面积:{}\n".format(
            self.name, self.__width * self.__length
        ))


r = Room('张宝富', 88, 100)
r.area()
