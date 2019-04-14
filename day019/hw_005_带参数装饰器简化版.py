# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-14 11:12
# 文件名称: hw_005_带参数装饰器简化版.py
# 开发工具: PyCharm

# 外层接收参数
def time(time):
    # 内层接收函数并执行装饰器逻辑
    def inner(f):
        for i in range(time):
            f()
        # 装饰完以后,还需要将函数返回,以便调用
        return f

    # 返回内层,以便装饰器生效
    return inner


@time(33)
def show():
    print("人生苦短,我用Python")


show()
