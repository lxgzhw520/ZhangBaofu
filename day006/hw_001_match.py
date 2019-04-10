# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/4/6 16:57
# 文件名称: hw_001_match.py
# 开发工具: PyCharm

# re.match 尝试从字符串的起始位置匹配一个模式，
# 如果不是起始位置匹配成功的话，match()就返回none。

# re.match(pattern, string, flags=0)

# 我们可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式
# 模块
import re

# 导入一个  模块

# 使用模块中各种方法

print(re.match('aaa', 'aaabbbccc'))
print(re.match('aaa', 'aaabbbccc').span())
print(re.match('aaa', 'aaabbbccc'))
