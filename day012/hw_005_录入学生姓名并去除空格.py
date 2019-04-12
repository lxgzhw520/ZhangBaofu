# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-12 09:38
# 文件名称: hw_005_录入学生姓名并去除空格.py
# 开发工具: PyCharm

# 需求:循环录入学生姓名,并移除其中的空格
# 分析:用while循环解决
# 用列表装学生的名字

# 1 定义一个空列表装学生名字

# 2 循环录入,在录入之前就去除空格,然后装进列表

# 3 打印列表

students = []
while True:
    name = input("姓名:").strip()
    students.append(name)
    print("%s 录入成功.是否继续? y/n:\n" % name)
    key = input()
    if key == 'n':
        break
print(students)
