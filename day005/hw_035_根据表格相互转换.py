# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/4/5 17:46
# 文件名称: hw_035_根据表格相互转换.py
# 开发工具: PyCharm

intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)  # 制作翻译表

str = "this is string example....wow!!!"
print(str.translate(trantab))
