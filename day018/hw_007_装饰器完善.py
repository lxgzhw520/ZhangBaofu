# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-14 08:09
# 文件名称: hw_007_装饰器完善.py
# 开发工具: PyCharm

def big_print1(f):
    # 在装饰器的内部再写一个函数
    def inner():
        import time  # 时间模块
        start = time.time()  # 得到开始时间
        ret = f()
        end = time.time()
        print("总共耗时: %.2f秒" % (end - start))
        return ret  # 将函数的执行结果返回

    # 外部返回内部函数
    return inner


# 不过这种方法有个坑,就是调用的时候不能加括号
@big_print1
def big_print():
    time = 10000 * 10
    for i in range(time):
        print("人生苦短,我用Python 第%s次" % (i + 1))


# 解决之前装饰器装饰以后不能加括号的问题
big_print()
