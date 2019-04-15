# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 11:17
# 文件名称: hw_006_自定义数组类.py
# 开发工具: PyCharm
# 需求:自定义一个数组类,实现数组的增删改查四个方法

class my_list:
    # 可以传入任意多个数,构成数组
    def __init__(self, *args):
        self.list = []
        for i in args:
            self.list.append(i)

    def add(self, num):
        self.list.append(num)
        print("添加成功")

    def delete(self, num):
        index = self.list.index(num)
        del self.list[index]
        print("删除成功")

    def update(self, old_num, new_num):
        index = self.list.index(old_num)
        self.list[index] = new_num
        print("修改成功")

    def query(self, num):
        index = self.list.index(num)
        if index:
            print("您要查找的数数是:{}\n已找到,索引是:{}\n".format(
                num, index
            ))
        else:
            print("暂无此数,请确认后重新输入.")

    # 打印列表
    def show(self):
        print(self.list)


# 实例化
l = my_list(1, 2, 3, 3, 4, 5, 5, 6, 888)
l.add(333)
l.show()
l.delete(2)
l.update(3, 223)
l.show()
l.query(4)
