# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-14 10:32
# 文件名称: hw_001_装饰器复习.py
# 开发工具: PyCharm

# 基础的装饰器
from functools import wraps  # 这个是别人写好的装饰器


# 一般用于装饰内部


def wrapper(func):
    # 给内部函数添加了一个装饰器
    @wraps(func)
    def inner(*args, **kwargs):
        print("在函数执行之前的逻辑...")
        import time
        start = time.time()
        ret = func(*args, **kwargs)  # 被装饰的函数
        print("在函数执行之后的逻辑...")
        end = time.time()
        print("共耗时:%.2f秒" % (end - start))
        return ret

    return inner


@wrapper
def show():
    for i in range(100000):
        print("人生苦短,我用Python 第%s次" % (i + 1))


show()
