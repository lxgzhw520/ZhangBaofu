# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 11:35
# 文件名称: hw_006_用logging替代print.py
# 开发工具: PyCharm
import logging

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)
fh = logging.FileHandler('log.log', encoding='utf-8')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

for i in range(100):
    logging.info("人生苦短,我用Python  第%d次" % (i + 1))
