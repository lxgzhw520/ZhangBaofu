# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-14 08:05
# 文件名称: hw_006_装饰器.py
# 开发工具: PyCharm

# 装饰器就是把闭包写成@
def big_print1(f):
    import time  # 时间模块
    start = time.time()  # 得到开始时间
    f()  # 执行打印
    end = time.time()
    print("总共耗时: %.2f秒" % (end - start))


# 不过这种方法有个坑,就是调用的时候不能加括号
@big_print1
def big_print():
    time = 10000 * 10
    for i in range(time):
        print("人生苦短,我用Python 第%s次" % (i + 1))


big_print
