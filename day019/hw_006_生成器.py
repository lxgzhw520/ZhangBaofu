# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-14 11:15
# 文件名称: hw_006_生成器.py
# 开发工具: PyCharm

# 函数中将return替换为yield就变成了生成器
# 比如:生成1-100个数字

def num():
    for i in range(100):
        return i


# 直接执行 会返回0  因为return会中断函数的执行
print(num())


def num1():
    for i in range(100):
        yield i


# <generator object num1 at 0x118bb9390>
# 直接执行得到的是函数信息 提示是一个装饰器
print(num1())

# 生成器的特点,值是动态生成的,节省内存
# 比如说这个生成器
# 会依次返回0-99
# 怎么取呢,一般都是用for循环
for i in num1():
    print(i)
    print('--' * 22)
    print(i)

# 第二次取是第二次生成
for i in num1():
    print('--' * 22)
    print(i)
    break
