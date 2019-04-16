# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-16 10:14
# 文件名称: hw_004_md5.py
# 开发工具: PyCharm
import hashlib  # 提供摘要算法的模块  一堆算法

# md5 用的最多的
# sha系列算法


md5 = hashlib.md5()
# 传入一个需要加密的字符串
md5.update(b'adsafsdfsaf')
# 转换为16进制的表示方法
print(md5.hexdigest())

# 不管用什么算法  使用方法都一样
# sha算法,随着算法复杂程度的增加,时间成本和空间成本都会增加
# 所以 一般用md5就够用了
sha1 = hashlib.sha1()
sha1.update(b'fslfjowirowierjoiwejroiw')
print(sha1.hexdigest())

# 一般用途:密码存储,文件的一致性认证
