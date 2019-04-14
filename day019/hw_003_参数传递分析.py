# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-14 11:01
# 文件名称: hw_003_参数传递分析.py
# 开发工具: PyCharm

# 定义第一层函数,用于接收参数
def time(time):
    # 定义第二层函数,用于接收函数
    def wrapper(f):
        # 定义第三层函数,用于执行装饰逻辑
        def inner():
            # 这里可以写一些装饰逻辑,比如计算执行时间
            for i in range(time):
                f()
            # 这里可以写一些函数执行完后的装饰逻辑
            # 最终要把这个函数返回 不然没法调用
            return f

        # 返回装饰逻辑函数,用于实现@装饰
        return inner

    # 返回装饰器 用于将整个逻辑返回
    return wrapper


@time(33)
def show():
    print("人生苦短,我用Python")


# 记住一个简单的结论,带参数的装饰器需要嵌套三层
show()
