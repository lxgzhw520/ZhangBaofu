# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 09:08
# 文件名称: hw_001_递归求斐波那契数列.py
# 开发工具: PyCharm

"""
斐波那契数列
1 1 2 3 5 f(n) f(n)+f(n-1)
规律 从第3个数起,每一个数都等于前两个数之和
"""


# 需求,定义一个函数,能求斐波那契数列的任意第n项

def fib(n):
    # 递归的终止语句是return
    # 一定要放在递归调用前面
    if n <= 2:
        return 1
    else:
        # 第n项等于前两项之和
        # 前两项分别是 fib(n-1) fib(n-1)
        return fib(n - 1) + fib(n - 2)


print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
