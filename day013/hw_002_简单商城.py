# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-12 21:57
# 文件名称: hw_002_简单商城.py
# 开发工具: PyCharm

"""
需求:
1.定义商品列表,用户登录系统的时候展示
2.用列表+字典实现注册功能
3.用户选择商品,展示商品详细信息
4.用户确认购买,计算总价
5.完成订单并发货,库存减少
"""

"""
暂时不考虑注册-较复杂,后面单独讲
分析:
1. 需要的数据
    商品表 [商品1,商品2...]
    用户表 [{用户1},{用户2}]
    商品详情表 {商品数据}
2. 要实现的功能
    1.展示所有商品
    2.用户选择商品后显示商品详情
    3.用户购买的时候计算价格
    4.确认用户是否支付
    5.购买成功后减少库存
"""

# 1.定义数据
goods = ['衣服', '手机', '包包']
goods_detail = [
    {
        "name": '衣服',
        'count': 100,
        'price': 999,
    },
    {
        "name": '手机',
        'count': 100,
        'price': 888,
    },
    {
        "name": '包包',
        'count': 100,
        'price': 18888,
    },

]
# 2.展示数据
while True:
    print('--' * 22)
    print('商品列表')
    for i in goods:
        print("%s : %s\n" % (goods.index(i) + 1, i))
    i = input("请输入您要查看的商品:")
    try:
        i = int(i) - 1
        if goods_detail[i]:
            print(
                "商品名称: %s\n"
                "商品数量: %s\n"
                "商品价格: %s\n" % (
                    goods_detail[i]['name'],
                    goods_detail[i]['count'],
                    goods_detail[i]['price'],
                )

            )
            print('--' * 22)
            print("是否购买? y/n")
            if input() == 'y':
                count = int(input("请输入购买数量:"))
                print("您要购买的是:%s,共%s件,需要支付%s元,请确认后付款." % (
                    goods_detail[i]['name'],
                    count,
                    goods_detail[i]['price'] * count,
                ))
                print("是否确认支付? y/n")
                if input() == 'y':
                    print("恭喜您成功支付,商品将不久后送到您的手上.")
                else:
                    print("您已取消支付.")
    except Exception as e:
        print(e)
        print("输入错误.")
    print("是否继续购物? y/n")
    if input() == "n":
        print("即将退出系统,欢迎下次再来.")
        break
