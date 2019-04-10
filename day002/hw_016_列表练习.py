# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/4/3 21:28
# 文件名称: hw_016_列表练习.py
# 开发工具: PyCharm

# Python 列表综合练习
#
# 使用 python 语言创建空列表 score，按学号顺序（由小到大）保存多个学生
# 一门课程的考试成绩。调用列表操作的常用函数实现以下功能：
# 1）创建一个空列表 score；
score = [68, 87, 59, 100, 59, 88, 54, 89, 76, 61]

# 2）调用append()函数在 score 列表中依次追加 10 个数值
# （68,87,92,100,76,88,54,89,76,61）；
# score.append()


# 3）输出score 列表中第 3 个元素的数值；
print(score[2])

# 4）输出score 列表中第 1~6 个元素的值；
print(score[1:7])

# 5）调用insert()函数，在 score 列表第3 个元素之前添加数值 59；
score.insert(2, 59)
print(score)

# 6）利用变量 num 保存数值 76,调用 count()函数，查询 num 变量值在 score 列表
# 中出现的次数；
num = 76
print(score.count(76))

# 7）使用in 查询score列表中是否有num 变量值的考试成绩；
if num in score:
    print('有')
else:
    print('没有')

# 8）调用index()函数，查询 score 列表中成绩是满分的学生索引；
# 100
# score = [68, 87, 92, 100, 76, 88, 54, 89, 76, 61]
# print()

# for i in range(len(score)):
#     if index(i)==100:
#         print(i)

count = 0
print(score)
# exit() 能够强行终止程序的执行
for i in score:
    if i == 100:
        print("成绩是满分的学生的索引是:", count)
        break
    count += 1

print('满分的同学的索引是:', score.index(100))
# 列表
# 返回的是:找到的第一个满足条件的数的索引
score = [68, 87, 92, 100, 76, 88, 54, 100, 89, 76, 100, 61]
# 咱们自己去封装函数 或者 用最基本的办法去解决

# 9）score 列表中将 59分加1 分；
# 遍历 找到所有59分的 +1
print('---' * 22)
score = [68, 87, 59, 100, 59, 88, 54, 89, 76, 61]
print(score)
for i in score:
    if i == 59:
        # 怎么+1
        # 需要得到索引
        score[score.index(i)] += 1
print(score)
print('---' * 22)


score = [68, 87, 59, 100, 59, 88, 54, 89, 76, 61]
# 10）调用del()函数删除 score 列表中第1 个元素；
# 11）调用len()函数获得 score 列表中元素的个数；
# 12）调用sort()函数，对列表中所有元素进行排序，输出考试的最高分和最低分；
# 13）调用reverse()函数，颠倒score 列表中元素的顺序；
# 14）调用pop()函数删除 score 列表中尾部的元素，返回删除的元素；
# 15）score 列表中追加数值 88，并输出。调用 remove()函数删除 score 列表中第
# 一个数值88；
# 16）创建2 个列表 score1 和score2， score1 中包含数值2 个元素值： 80,61， score2
# 中包含3 个元素值：71,95，82，合并这两个列表，并输出全部元素；
# 17）创建score1 列表，其中包含数值 2 个元素值：80,61，将 score1中元素复制
# 5 遍保存在score2 列表中，输出score2 列表中全部元素。
