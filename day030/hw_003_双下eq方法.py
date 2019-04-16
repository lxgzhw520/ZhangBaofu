# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 09:50
# 文件名称: hw_003_双下eq方法.py
# 开发工具: PyCharm

class A:
    def __init__(self, name):
        self.name = name


a = A('AAA')
b = A('AAA')

# 默认比较内存地址
print(a == b)
print('--' * 22)
print('--' * 22)


class A:
    def __init__(self, name):
        self.name = name

    # 重写以后就根据自定义的方法比较
    def __eq__(self, other):
        # 使用==时自动触发
        if self.name == other.name:
            return True
        else:
            return False


a = A('AAA')
b = A('AAA')

# 默认比较内存地址
print(a == b)
