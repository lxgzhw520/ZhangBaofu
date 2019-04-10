# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/4/6 17:07
# 文件名称: hw_004_compile.py
# 开发工具: PyCharm

# compile 函数用于编译正则表达式，
# 生成一个正则表达式（ Pattern ）对象
import re

pattern = re.compile('111')
print(pattern.findall('111222111'))

# compile 编译
# 作用:将一个正则表达式 编译为一个可复用 表达式,进行匹配
# 一般不会独立使用 通常配合re.findall()
