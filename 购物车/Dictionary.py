#!/usr/bin/env python
# -*- coding:utf-8 -*-
#功能要求：
# 要求用户输入总资产，例如：2000
# 显示商品列表，让用户输入商品名称，加入购物车
# 购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
# 附加：可充值、某商品移除购物车

#用字典构造以购买产品，购物车
#用户输入总资产
zong_zi_chan = input("请输入你的总资产")
#将用户输入总资产转换成数字类型
zong_zi_chan1 = int(zong_zi_chan)
#打印出总资产
print("您的总资产为",zong_zi_chan1,"元")
print("\n")

#产品字典
shang_pin = [
    {"名称":"手机", "价格":200},
    {"名称":"电脑", "价格":300},
    {"名称":"水笔", "价格":10},
    {"名称":"纸张", "价格":20},
]
print("可购买产品有:")
for i in shang_pin:
    #循环出产品字典里的名称和价格
    print(i["名称"],i["价格"],"元")

print("\n")
#以购买的产品
gou_mai2 = {}
#循环购买模块
while True:
    #用户输入要购买的产品名称
    gou_mai = input("请输入要购买的商品名称,输入y结算")
    #将用户输入的信息进行判断，如果用户输入的是y退出循环购买模块
    if gou_mai.lower() == "y":
        break
    else:#如果用户输入不是y执行下面
        for i in shang_pin:
            #判断循环到的产品名称如果等于用户输入的购买名称
            if i["名称"] == gou_mai:
                #将循环到的赋值给一个变量
                chan_pin = i["名称"]
                #判断循环到的名称在已购买产品字典里是否存在这个键
                if chan_pin in gou_mai2.keys():
                    #如果存在将已购买产品字典里本条数据的数量加1
                    gou_mai2[chan_pin]["数量"] = gou_mai2[chan_pin]["数量"] + 1
                else:
                    #如果不在将已购买产品字典里，将本条数据更新到已购买产品字典里，默认数量1
                    gou_mai2[chan_pin] = {"价格":i["价格"], "数量":1}
                #打印已购买产品
                print(gou_mai2)

print("\n")
print("您以购买的商品有:")
#购买产品的所有共计费用
gong_ji = 0
#循环出以购买产品字典里的键和值
for k,v in gou_mai2.items():
    #将字典里的价格赋值给一个变量
    jia_ge = v["价格"]
    #将字典里的数量赋值给一个变量
    shu_liang = v["数量"]
    #将数量乘以价格等于每样产品的总价
    zong_jia = shu_liang * jia_ge
    #打印出以购买的每样产品的价格，数量，总价
    print(k,"价格", v["价格"], "数量", v["数量"], "总价=",zong_jia)
    #每次循环累计共计加总价等于共计消费
    gong_ji += zong_jia
#打印出共计费用
print("共计:",gong_ji)

#判断总资产如果大于或者等于共计费用，购买成功，如果总资产小于共计费用说明资金不够
if zong_zi_chan1 >= gong_ji:
    print("恭喜你购买成功")
else:
    print("对不起你的资金不够，请充值")