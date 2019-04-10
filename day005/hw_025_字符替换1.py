# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/4/5 17:31
# 文件名称: hw_025_字符替换-重要.py
# 开发工具: PyCharm

# 生成 翻译
# str.maketrans(intab, outtab)
# 进行 翻译translate
s = str.maketrans('145', '一二三')
print('111122223334444555'.translate(s))

# 80.90
# print('80.90'.translate(str.maketrans('80.90', '八十点九零')))
