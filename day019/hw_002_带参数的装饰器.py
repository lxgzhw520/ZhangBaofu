# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-14 10:51
# 文件名称: hw_002_带参数的装饰器.py
# 开发工具: PyCharm

# 打印指定次数
def time(time):
    def wrapper(f):
        def inner(*args, **kwargs):
            # 执行time次函数的调用
            for i in range(1, time + 1):
                f(*args, **kwargs)
            # 关键点 最终一定要返回被装饰的函数
            return f

        # 返回内部装饰
        return inner

    # 返回装饰器
    return wrapper


@time(33)
def show():
    print("人生苦短,我用Python")


show()
