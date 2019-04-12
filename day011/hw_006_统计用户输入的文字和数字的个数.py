# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-12 08:58
# 文件名称: hw_006_统计用户输入的文字和数字的个数.py
# 开发工具: PyCharm

# 需求:用户输入任意字符 统计其中的数字和非数字的格式并格式化输出

# 分析
# 1 获取用户输入
s = input("请输入:")
# 2 遍历用户输入,判断是否为数字
# 2.1 定义两个统计变量,分别统计数字和非数字
# 2.2 格式化输出  %d
# for i in s:
#     # print(i)
#     # 测试
#     # eval 能够将字符串中的数字转换为Python中的数字类型
#     if type(eval(i)) is int:
#         print(i)

# 通过以上方法得出的结论,进行解题
# 定义两个统计变量
str_count = 0
num_count = 0
# 新知识:捕获异常 try
for i in s:
    # if type(eval(i)) is int:
    try:
        int(i)
        num_count += 1
    except Exception as e:
        # print(e)
        str_count += 1

    # if int(i):
    #     num_count += 1
    # else:
    #     str_count += 1
print("您总共输入了%d个数字,%d个非数字." % (num_count, str_count))
