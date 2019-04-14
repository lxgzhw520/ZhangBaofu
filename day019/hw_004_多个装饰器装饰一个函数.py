# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-14 11:05
# 文件名称: hw_004_多个装饰器装饰一个函数.py
# 开发工具: PyCharm

# 一个函数可以有多个装饰器
# 比如 执行打印10000次 人生苦短,我用Python
# 1 添加计算执行时间的功能
# 2 在执行之前我需要先提示用户即将开始

def time(time):
    def wrapper(f):
        def inner(*args, **kwargs):
            import time as t
            start = t.time()
            for i in range(time):
                f()
            end = t.time()
            print("共耗时 %.2f秒" % (end - start))
            return f

        return inner

    return wrapper


def info(f):
    def inner():
        print("程序即将开始....")
        f()
        return f

    return inner


@info
@time(10)
def show():
    print("人生苦短,我用Python")


show()
