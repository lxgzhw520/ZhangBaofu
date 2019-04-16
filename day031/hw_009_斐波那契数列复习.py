# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 11:43
# 文件名称: hw_009_斐波那契数列复习.py
# 开发工具: PyCharm
import logging

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)
fh = logging.FileHandler('log.log', encoding='utf-8')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)


def fab(n):
    if n <= 2:
        return 1
    else:
        return fab(n - 1) + fab(n - 2)


logging.info(fab(1))
logging.info(fab(2))
logging.info(fab(3))
logging.info(fab(4))
logging.info(fab(5))
