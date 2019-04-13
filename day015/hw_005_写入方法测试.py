# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-13 08:56
# 文件名称: hw_005_写入方法测试.py
# 开发工具: PyCharm

# 这种方法不可取
# with open('README.md', mode='r+', encoding='utf8') as f:
#     f.write('\n## 这里是测试方法\n- 测试一下是否成功')

# with open('README.md', mode='w+', encoding='utf8') as f:
#     f.write('')  # 会直接清空
#     print(f.read())

with open('README.md', mode='w+', encoding='utf8') as f:
    content = '# 文件操作'
    f.write(content)
    print(f.read())
