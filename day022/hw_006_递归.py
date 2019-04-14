# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-15 07:35
# 文件名称: hw_006_递归.py
# 开发工具: PyCharm

# 递归就是自己调用自己,本质是一种循环


i = 0
while True:
    print("人生苦短,我用Python 第{}次".format(i + 1))
    i += 1
    if i >= 10:
        break

# 递归的写法
j = 0


def show():
    global j
    print("人生苦短,我用Python 第{}次".format(j + 1))
    j += 1
    # 终止判断要写在递归调用前面
    if j >= 10:
        return  # 递归的终止语句是return
    show()  # 递归需要自己调用自己


print('--' * 22)
# 递归需要主动调用
show()
