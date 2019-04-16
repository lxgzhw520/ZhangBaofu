# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 11:16
# 文件名称: hw_003_日志配置.py
# 开发工具: PyCharm
import logging

# 可以创一个name 默认是root
logger = logging.getLogger()


fh = logging.FileHandler('log.log', encoding='utf-8')
sh = logging.StreamHandler()  # 创建一个屏幕控制对象
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter2 = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s [line:%(lineno)d] : %(message)s')
# 文件操作符 和 格式关联
fh.setFormatter(formatter)
sh.setFormatter(formatter2)
# logger 对象 和 文件操作符 关联
logger.addHandler(fh)
logger.addHandler(sh)

# 非常重要
logging.info('测试一下 info')  # 正常信息
logging.warning('测试一下 warning')
logging.error('测试一下 error')  # 错误信息
logging.critical('测试一下 critical')  # 高级别的 # 严重错误信息
