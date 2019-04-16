# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 11:16
# 文件名称: hw_003_日志配置.py
# 开发工具: PyCharm
import logging

# 可以创一个name 默认是root
logger = logging.getLogger()
# 配置日志记录的等级
logging.basicConfig(level=logging.INFO)

fh = logging.FileHandler('log.log', encoding='utf-8')
# asctime 本地时间
# name管理员
# levelname日志等级
# message日志信息
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# 文件操作符 和 格式关联
fh.setFormatter(formatter)
# logger 对象 和 文件操作符 关联
logger.addHandler(fh)

# 非常重要
logging.info('测试一下 info')  # 正常信息
logging.warning('测试一下 warning')
logging.error('测试一下 error')  # 错误信息
logging.critical('测试一下 critical')  # 高级别的 # 严重错误信息
