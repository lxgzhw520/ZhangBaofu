# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-17 06:51
# 文件名称: hw_006_正则复习.py
# 开发工具: PyCharm
import logging

logger = logging.getLogger(name="张大鹏")
logging.basicConfig(level=logging.INFO)
fh = logging.FileHandler('log.log', encoding='utf-8')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

# 正则复习
from requests import get

html = get("http://lxgzhw520.com")
# logging.info(html.text)
html = html.text

# 取出其中的所有图片
import re

pattern = re.compile(r'<.*?src="(.*?)".*?/>')
logging.info(pattern.findall(html, re.S))
