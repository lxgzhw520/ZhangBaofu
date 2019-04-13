# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-14 06:46
# 文件名称: hw_002_函数.py
# 开发工具: PyCharm

# 函数,定义了以后,可以在任何需要使用它的地方调用

# 定义一个函数,打印100次  人生苦短,我用Python
def show_python():
    # 函数定义以后不会立即执行,只有在调用的时候才会执行
    for i in range(100):
        print("人生苦短,我用Python")


# 调用
show_python()


# 带参数的函数
# 需求:定义一个函数,我让他打印多少次,他就打印多少次 人生苦短,我用Python
def show_python(time):
    # 写在括号中的叫做参数
    # 定义了参数,在调用的时候就必须传
    for i in range(time):
        print("人生苦短,我用Python:", i)


show_python(10)
