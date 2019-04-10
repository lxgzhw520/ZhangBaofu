# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/4/5 17:31
# 文件名称: hw_025_字符替换-重要.py
# 开发工具: PyCharm

intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)

str = "this is string example....wow!!!"
print(str.translate(trantab))

print('1aaa23bbb45'.translate(str.maketrans('12345', '一二三四五')))
