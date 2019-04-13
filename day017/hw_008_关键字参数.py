# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-14 07:22
# 文件名称: hw_008_关键字参数.py
# 开发工具: PyCharm


# 前面学过了默认参数,当我们需要传不限长度的默认参数的时候,就可以用关键字参数
# 关键字参数用**定义

# 关键字参数的类型
def show_info(**kwargs):
    print(type(kwargs))


# <class 'dict'>
# 通过打印测试,我们很容易就知道了,关键字参数实际上是一个字典
# 所以,我们可以通过字典的方法来处理关键字参数
show_info()

# 定义一个方法,能够自由的传入一个人的信息并打印
# 先复习
d = {'name': '李珂瑶', 'age': 18, 'gender': '女'}
# 返回字典中的每一项键值对
print(d.items())
# 返回字典中键的列表
print(d.keys())
# 返回字典中值的列表
print(d.values())


def show_info(**kwargs):
    for i in kwargs.items():
        # print(i)  # 得到每一项
        # 打印
        print('%s' % i[0].center(22, '-'))
        print(i[1])


show_info(name='李珂瑶', age=18, gender='女')
