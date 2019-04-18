# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-17 09:29
# 文件名称: main.py
# 开发工具: PyCharm
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# 定义hw_001-hw_010是个路由
@app.route('/hw_001.html')
def hw_001():
    return render_template('hw_001.html')


@app.route('/hw_002.html')
def hw_002():
    return render_template('hw_002.html')


@app.route('/hw_003.html')
def hw_003():
    return render_template('hw_003.html')


@app.route('/hw_004.html')
def hw_004():
    return render_template('hw_004.html')


@app.route('/hw_005.html')
def hw_005():
    return render_template('hw_005.html')


@app.route('/hw_006.html')
def hw_006():
    return render_template('hw_006.html')


@app.route('/hw_007.html')
def hw_007():
    return render_template('hw_007.html')


if __name__ == '__main__':
    app.run(debug=True)
