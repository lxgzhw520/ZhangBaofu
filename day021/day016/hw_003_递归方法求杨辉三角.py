# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 09:23
# 文件名称: hw_003_递归方法求杨辉三角.py
# 开发工具: PyCharm

"""
杨辉三角
　　　　　　　　１
　　　　　　　１　１
　　　　　　１　２　１
　　　　　１　３　３　１
　　　　１　４　６　４　１
　　　１　５　10　10　５　１
　　１　６　15　20　15　６　１
　１　７　21　35　35　21　７　１
１　８　28　56　70　56　28　８　１

观察规律
把大的三角形拆分为无数小的 顶点在下的倒三角形
三角形的顶点=另外两个顶点的和

看成是一种特殊的数列
项  注意:把每一列看成是一个数列
l1  1
l2  1 1
l3  1 2 1
l4  1 3  3  1
l5  1 4  6  4  1
......
假设上一列为ln 这一列为lm
lm  1 ln[0]+ln[1]  ln[1]+ln[2]....ln[n-1]+ln[n] 1
"""


# 输入行号,就能够打印整行的杨辉三角
def yang_hui(n):
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 1]
    else:
        new_list = [1]
        # 遍历前一个杨辉三角,将每两个数之和组成一个新的列
        for i in range(len(yang_hui(n - 2))):
            new_list.append(yang_hui(n - 1)[i] + yang_hui(n - 1)[i + 1])
        new_list.append(1)
        return new_list


print(yang_hui(0))
print(yang_hui(1))
print(yang_hui(2))
print(yang_hui(3))
print(yang_hui(4))
print(yang_hui(5))
