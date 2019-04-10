# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019/4/8 19:31
# 文件名称: 问题.py
# 开发工具: PyCharm

s = """
<tr class="odd">
                    	<th>货币名称</th>
                        <th>现汇买入价</th>
                        <th>现钞买入价</th>
                        <th>现汇卖出价</th>
                        <th>现钞卖出价</th>
                        <th>中行折算价</th>
                        <th>发布日期</th>
                        <th>发布时间</th>
                    </tr>
"""
import re

pattern = re.compile(r'<th>(\w*?)</th>')
print(pattern.findall(s)[:11])
