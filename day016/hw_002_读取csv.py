# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-13 09:53
# 文件名称: hw_002_读取csv.py
# 开发工具: PyCharm

# 需求 读取csv中的数据
score_list = []
with open('score.csv', 'r+') as f:
    # print(f.read())
    # 读取一行
    # 得到的是一个数组
    # print(f.readlines())
    scores = f.readlines()
    # 对分数进行处理
    # 1 去掉为空的 '\n'的数据
    # 2 将剩下的数据切割
for i in scores:
    # print(i)
    if not i.isspace():
        # print(i)
        score_list.append(i.split(','))

# 打印分数列表
print(score_list)
for i in score_list:
    print(i)
