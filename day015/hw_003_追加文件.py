# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-13 08:50
# 文件名称: hw_003_追加文件.py
# 开发工具: PyCharm

f = open('README.md', mode='a+', encoding='utf8')

# 写入
f.write('\n- 追加文件用a+')
print('追加成功')
f.close()
