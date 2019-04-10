# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/4/8 17:17
# 文件名称: hw_001_匹配列表.py
# 开发工具: PyCharm


s = """
<table>
    <tr>
        <td>第1列</td>
        <td>第2列</td>
        <td>第3列</td>
        <td>第4列</td>
    </tr>
</table>
"""
import re

pattern = re.compile(r'<td>([\s\S]*?)</td>')
print(pattern.findall(s))
