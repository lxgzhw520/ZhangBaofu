# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-17 08:54
# 文件名称: hw_001_第一个Flask程序.py
# 开发工具: PyCharm
from flask import Flask
from log import logger

app = Flask(__name__)


@app.route('/')
def index():
    return "第一个Flask程序"


if __name__ == '__main__':
    app.run(debug=True)
