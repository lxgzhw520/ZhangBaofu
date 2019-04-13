# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-14 06:32
# 文件名称: hw_001_文件操作.py
# 开发工具: PyCharm
with open('score.csv', 'w') as f1:
    f1.write("姓名,年龄,性别,班级,语文分数,数学分数,英语分数\n")
    f1.write("张大鹏,22,男,Python001,88,77,78\n")
    f1.write("李珂瑶,18,女,Python001,99,99,99\n")
# with open 可以同时打开两个文件
with open('score.csv', 'r+') as f1, open('score.back.csv', 'a+') as f2:
    # print(f1.readlines())
    # print(f1.readlines())
    # 会一行一行的读取,一行一行的打印
    for i in f1:
        # print(i)
        if '99' in i or '姓名' in i:
            print(i)
            f2.write(i)

import os

# 删除文件和命名文件
os.remove('score.csv')  # 删除文件
os.rename('score.back.csv', 'score.csv')  # 重命名
