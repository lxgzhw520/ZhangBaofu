# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-12 21:43
# 文件名称: hw_001_学生成绩管理系统.py
# 开发工具: PyCharm

# 需求:录入学生分数,将>90分的 >80  > 60 <60的,分到字典四个键中
# 最终 {"优秀":[],"良好":[],"中等":[],"较差":[]}


# 1 定义一个空字典,并设置好结构,便于存储
score = {
    "优秀": [],
    "良好": [],
    "中等": [],
    "较差": [],
}
# 2 循环录入数据,并判断分数,分别存储
while True:
    new_score = input("分数:")
    try:
        new_score = int(new_score)
        if new_score > 100 or new_score < 0:
            print("输入错误,请检查后重新输入.")
        else:
            if new_score > 90:
                score['优秀'].append(new_score)
            elif new_score > 80:
                score['良好'].append(new_score)
            elif new_score > 60:
                score["中等"].append(new_score)
            else:
                score['较差'].append(new_score)
            print("分数录入成功.是否继续?y/n")
        if input() == 'n':
            break
    except Exception as e:
        print(e)

# 3 打印测试
for i in score:
    print(i, ':\t', score[i])
