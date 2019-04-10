# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/4/5 17:14
# 文件名称: hw_010_制表符转换为空格.py
# 开发工具: PyCharm

str = "this is\tstring example....wow!!!"

print("原始字符串: " + str)
print("替换 \\t 符号: " + str.expandtabs())
print("使用16个空格替换 \\t 符号: " + str.expandtabs(16))
