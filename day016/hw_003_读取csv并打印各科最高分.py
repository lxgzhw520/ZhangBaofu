# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-13 10:02
# 文件名称: hw_003_读取csv并打印各科最高分.py
# 开发工具: PyCharm

# 通过前面的分析,我们很容易拿到学生列表
with open('score.csv', 'r') as f:
    scores = f.readlines()

# 定义各科的最高分
english_max = chinese_max = math_max = 0
# 定义各科的最高分同学
english_max_student = chinese_max_student = math_max_student = ''
for i in scores:
    if not i.isspace():
        # 很容易就发现,各科成绩是列表的最后三个
        # 现在只需要对这三个数据进行处理即可
        print(i.split(','))
        student = i.split(',')
        # 语文
        # print(student[-3])
        try:
            # 语文最高分
            if int(student[-3]) > chinese_max:
                chinese_max = int(student[-3])
                # 姓名
                chinese_max_student = student[0]
            # 英语最高分
            if int(student[-2]) > english_max:
                english_max = int(student[-2])
                # 姓名
                english_max_student = student[0]
            # 数学最高分
            if int(student[-1]) > math_max:
                math_max = int(student[-1])
                # 姓名
                math_max_student = student[0]
        except Exception as e:
            print(e)
        # 英语
        # print(student[-2])
        # 数学
        # print(student[-1])

# 打印测试
print('语文:', chinese_max_student, chinese_max)
print('英语:', english_max_student, english_max)
print('数学:', math_max_student, math_max)
