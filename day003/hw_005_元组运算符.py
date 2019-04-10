# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/4/3 21:22
# 文件名称: hw_005_元组运算符.py
# 开发工具: PyCharm

# len() + * in for in

t = (1, 2, 3)

print(len(t))
print(t + t)
print(t * 3)
print(3 in t)
for i in t:
    print(i)
