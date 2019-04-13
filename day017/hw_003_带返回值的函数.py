# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-14 06:51
# 文件名称: hw_003_带返回值的函数.py
# 开发工具: PyCharm


# 定义一个函数,能够计算加法
# 最简单的
def add01():
    print("%s + %s = %s" % (3, 3, 6))


# 带参数的
def add02(a, b):
    print("%s + %s = %s" % (a, b, a + b))


# 带参数的 带返回值的
def add03(a, b):
    print("%s + %s = %s" % (a, b, a + b))
    # return 用来返回函数的执行结果
    return a + b


# 调用
add01()
add02(33, 33)
add03(33, 33)
# 凡是带返回值的 都可以用变量来接收
result = add03(44, 55)
print(result)
# 也可以直接打印
print(add03(44, 55))
