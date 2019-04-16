# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 11:36
# 文件名称: hw_007_用logging记录异常.py
# 开发工具: PyCharm
import logging

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)
fh = logging.FileHandler('log.log', encoding='utf-8')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)
while True:
    try:
        num1 = int(input("请输入第一个数:"))
        num2 = int(input("请输入第二个数:"))
        logging.info("%d + %d = %d" % (num1, num2, num1 + num2))
        if input('是否退出?y/n') == 'y':
            break
    except Exception as e:
        logging.error(e)
