# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-13 09:13
# 文件名称: hw_009_学生成绩管理系统.py
# 开发工具: PyCharm

# 需求:创建一个文件,每一行是一个学生的信息
# 需要包含:姓名,年龄,性别,班级,语文分数,英语分数,数学分数
# 以csv格式存储

# 分析:循环录入,a+模式

# 1 先创建文件,然后写入第一行 姓名,年龄,性别,班级,语文分数,英语分数,数学分数
# 2 循环录入,将数据填充到每一行

with open('StudentScores.csv', 'a+') as f:
    f.write('姓名,年龄,性别,班级,语文分数,英语分数,数学分数\n')
    while True:
        try:
            name = input("姓名:")
            age = int(input("年龄:"))
            gender = input("性别:")
            class_no = input("班级:")
            chinese_score = float(input('语文分数:'))
            english_score = float(input('英语分数:'))
            math_score = float(input('数学分数:'))
            # 将新学生的信息进行拼接并存储
            new_score = '%s,%s,%s,%s,%s,%s,%s\n' % (
                name, age, gender, class_no, chinese_score, english_score, math_score)
            f.write(new_score)
            if input('数据录入成功,是否继续? y/n:\t') == 'n':
                break
        except Exception as e:
            print(e)
            if input('数据录入错误,是否继续? y/n:\t') == 'n':
                break
    print('感谢您的使用,即将退出系统,欢迎下次再来!')
