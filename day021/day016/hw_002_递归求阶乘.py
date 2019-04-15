# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 09:14
# 文件名称: hw_002_递归求阶乘.py
# 开发工具: PyCharm

"""
阶乘
1!=1*1
2!=2*1
3!=3*2*1
n!=n*(n-1)*...*1

规律:
1.第一项为1
2.第2项起,每一项等于一个等差数列的乘积  等差为1
"""


# 普通方法实现
def factorial(n):
    sum = 1
    for i in range(1, n + 1):
        sum *= i
    return sum


print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))


# 递归方法实现
def fac(n):
    if n <= 1:
        # 如果到了1 就返回1
        return 1
    else:
        # 如果大于1 就一直递归成到1
        return n * fac(n - 1)


"""
分析
fac(1)
1

fac(2)
2*fac(2-1)

fac(3)
3*fac(2)
=3*2*fac(1)
=3*2*1

fac(4)
=4*fac(3)
=4*3*fac(2)
=4*3*2*fac(1)
=4*3*2*1
......
"""

print('--' * 22)
print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
