# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-13 06:58
# 文件名称: hw_002_字符串的常用方法.py
# 开发工具: PyCharm

# 字符串类的源码
class str(object):
    """
    str(object='') -> str
    str(bytes_or_buffer[, encoding[, errors]]) -> str
    根据给出的参数,返回新的字符串
    """

    def capitalize(self, *args, **kwargs):  # real signature unknown
        """
        将首字母大写,其余字母小写
        """
        pass

    def casefold(self, *args, **kwargs):  # real signature unknown
        """
        返回合适的字符串
        """
        pass

    def center(self, *args, **kwargs):  # real signature unknown
        """
        根据指定的长度将字符串居中,可以指定填充字符串
        """
        pass

    def count(self, sub, start=None, end=None):
        """
        S.count(sub[, start[, end]]) -> int
        统计指定字符串的格式,可以指定开始位置和结束位置
        """
        return 0

    def encode(self, *args, **kwargs):
        """
        字符串编码
        """
        pass

    def endswith(self, suffix, start=None, end=None):
        """
        S.endswith(suffix[, start[, end]]) -> bool
        判断是否以指定的后缀结尾,可以指定开始位置和结束位置
        """
        return False

    def expandtabs(self, *args, **kwargs):
        """
        返回一份复制的文本,将\t换成了8个空格
        """
        pass

    def find(self, sub, start=None, end=None):
        """
        S.find(sub[, start[, end]]) -> int
        返回最新找到的查找字符串位置,错误返回-1
        """
        return 0

    def format(self, *args, **kwargs):
        """
        S.format(*args, **kwargs) -> str
        返回格式化后的字符串
        """
        pass

    def format_map(self, mapping):
        """
        S.format_map(mapping) -> str
        返回格式化后的字符串,根据mapping对应关系
        """
        return ""

    def index(self, sub, start=None, end=None):
        """
        S.index(sub[, start[, end]]) -> int
        返回查找字符串的位置,如果没有 会报错
        """
        return 0

    def isalnum(self, *args, **kwargs):  # real signature unknown
        """
        判断是否为字母+数字的组合
        """
        pass

    def isalpha(self, *args, **kwargs):  # real signature unknown
        """
        判断是否都是字母
        """
        pass

    def isascii(self, *args, **kwargs):  # real signature unknown
        """
        判断是否都是ASCII码,空也算
        """
        pass

    def isdecimal(self, *args, **kwargs):  # real signature unknown
        """
        判断是否为十进制的字符串
        """
        pass

    def isdigit(self, *args, **kwargs):  # real signature unknown
        """
        判断是否为数字0-9组成的
        """
        pass

    def isidentifier(self, *args, **kwargs):  # real signature unknown
        """
        判断是否为Python的标识符
        用.iskeyword()也可以判断
        """
        pass

    def islower(self, *args, **kwargs):
        """
        判断是否为全部小写
        """
        pass

    def isnumeric(self, *args, **kwargs):  # real signature unknown
        """
        判断是否为数字
        """
        pass

    def isprintable(self, *args, **kwargs):
        """
        判断是否为可打印的
        """
        pass

    def isspace(self, *args, **kwargs):
        """
        判断是否为空格
        """
        pass

    def istitle(self, *args, **kwargs):  # real signature unknown
        """
        判断是否为标题,每个单词的首字母都大写
        """
        pass

    def isupper(self, *args, **kwargs):  # real signature unknown
        """
        判断是否为全大写
        """
        pass

    def join(self, ab=None, pq=None, rs=None):
        """
        把任意多个字符数组联系起来
        例如: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
        """
        pass

    def ljust(self, *args, **kwargs):  # real signature unknown
        """
        返回根据指定长度左对齐的文本
        """
        pass

    def lower(self, *args, **kwargs):  # real signature unknown
        """
        返回将字符串全部转换为小写后的复制文本
        """
        pass

    def lstrip(self, *args, **kwargs):  # real signature unknown
        """
        去掉字符串左边的空格
        """
        pass

    def maketrans(self, *args, **kwargs):
        """
        返回一个用于str.translate()的字典
        """
        pass

    def partition(self, *args, **kwargs):
        """
        返回分离成3元元素的元组
        """
        pass

    def replace(self, *args, **kwargs):
        """
        返回替换后的文本的复制
        """
        pass

    def rfind(self, sub, start=None, end=None):
        """
        S.rfind(sub[, start[, end]]) -> int
        从右边开始找,找不到返回-1
        """
        return 0

    def rindex(self, sub, start=None, end=None):
        """
        S.rindex(sub[, start[, end]]) -> int
        从右边开始找索引,找不到会报错
        """
        return 0

    def rjust(self, *args, **kwargs):  # real signature unknown
        """
        返回根据指定长度右对齐的文本
        """
        pass

    def rpartition(self, *args, **kwargs):
        """
        从右边分离
        """
        pass

    def rsplit(self, *args, **kwargs):  # real signature unknown
        """
        从右边分割,可以穿sep='分割字符串',maxsplit=最大分割次数
        """
        pass

    def rstrip(self, *args, **kwargs):  # real signature unknown
        """
        去掉右边的空格
        """
        pass

    def split(self, *args, **kwargs):  # real signature unknown
        """
        分割字符串,可以传sep,maxsplit两个参数等
        """
        pass

    def splitlines(self, *args, **kwargs):
        """
        根据换行符进行切割
        """
        pass

    def startswith(self, prefix, start=None, end=None):  # real signature unknown; restored from __doc__
        """
        S.startswith(prefix[, start[, end]]) -> bool
        判断是否以某个前缀开始
        """
        return False

    def strip(self, *args, **kwargs):  # real signature unknown
        """
        去掉空格
        """
        pass

    def swapcase(self, *args, **kwargs):  # real signature unknown
        """大小写相互转化"""
        pass

    def title(self, *args, **kwargs):  # real signature unknown
        """
        转换为标题格式
        """
        pass

    def translate(self, *args, **kwargs):  # real signature unknown
        """
        根据maketrans(self, *args, **kwargs)进行翻译
        """
        pass

    def upper(self, *args, **kwargs):  # real signature unknown
        """ 转换为大写"""
        pass

    def zfill(self, *args, **kwargs):  # real signature unknown
        """
        指定宽度,不满足宽度用0填充
        """
        pass
