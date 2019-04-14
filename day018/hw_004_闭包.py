# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-14 07:53
# 文件名称: hw_004_闭包.py
# 开发工具: PyCharm

# 闭包实际上就是 参数是函数,且返回值也是函数
# 是前面讲的两个内容的结合


# 应用:比如说我们遇到一个函数,希望不修改函数的结构就给这个函数添加功能
# 这个时候就可以用到闭包

# 实战

def big_print():
    # 打印1亿次人生苦短,我用Python
    # time = 10000 ** 2
    # 如果电脑性能较差就打印10万次
    time = 10000 * 10
    for i in range(time):
        print("人生苦短,我用Python 第%s次" % (i + 1))


# big_print()


# 现在 我们需要不修改源代码,就添加一个测试打印时间的功能
# 这就需要用到闭包了
def big_print1(f):
    import time  # 时间模块
    start = time.time()  # 得到开始时间
    f()  # 执行打印
    end = time.time()
    print("总共耗时: %.2f秒" % (end - start))


big_print1(big_print)
