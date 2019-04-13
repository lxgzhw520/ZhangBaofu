# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-13 09:09
# 文件名称: hw_008_录入学生分数并存储.py
# 开发工具: PyCharm

# 需求:不断的录入学生的分数,存储进score.txt
# 分析 a+ 追加模式  循环录入

with open('score.txt', 'a+') as f:
    while True:
        score = input("分数:") + '\n'
        f.write(score)
        if input('分数录入成功,是否继续? y/n') == 'n':
            break
