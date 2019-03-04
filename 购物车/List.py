#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 四、购物车
# 功能要求：
# 要求用户输入总资产，例如：2000
# 显示商品列表，让用户输入商品名称，加入购物车
# 购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
# 附加：可充值、某商品移除购物车

#用列表构造以购买产品，购物车
#默认总资产等于0
zong_zi_chan = 0
#要求用户输入总资产
zong_zi_chan1 = input("请输入总资产")
#判断用户输入的是否是纯数字
if zong_zi_chan1.isdigit():
    pass
else:
    exit("你输入的不是数字类型的资产")
#将用户输入的总资产转换成整数类型
zong_zi_chan = int(zong_zi_chan1)
#打印出用户输入的总资产
print("你的总资产为:",zong_zi_chan,"元")
#换行
print("\n")

print("可购买商品有:")
shang_pin = [
    {"名称":"手机", "价格":200},
    {"名称":"电脑", "价格":300},
    {"名称":"水笔", "价格":10},
    {"名称":"纸张", "价格":20},
]
#以购买商品
shang_pin2 = []
for i in shang_pin:
    #通过循环列表里面字典的键，来显示出商品和价格
    print(i["名称"], i["价格"], "元")
#换行
print("\n")

ming = ""
while True:
    #要求用户输入要购买的商品名称
    ming_cheng = input("输入y结算/请输入要购买的商品名称挑选商品")
    if ming_cheng == "y":#判断用户输入的是商品名称还是结算符
        break #如果用户输入的是结算符退出while进行结算
    else:
        for i in shang_pin:
            #循环产品列表，判断循环到的产品名称是否有等于用户输入的名称
            if i["名称"] == ming_cheng:
                #如果循环到的产品名称有等于用户输入的名称，将这个名称赋值给ming变量
                ming = i["名称"]
            else:
                pass
        #判断ming变量是否等于用户输入的
        if ming == ming_cheng:
            pass
        else:
            #如果不等于提示商品名称不存在，退出程序
            exit("你输入的商品名称不存在")
        for i in shang_pin:
            #循环商品列表，判断商品名称是否有等于用户输入的
            if i["名称"] == ming_cheng:
                #如果循环到的商品名称等于用户输入名称，将此商品字典追加更新到一个新列表，也就是用户
                shang_pin2.append(i)
        print("你以挑选了:",shang_pin2)
    zongjia = 0
for i in shang_pin2:
    danjia = i["价格"]
    zongjia += danjia
print("现在开始结算共计:", zongjia, "元")
if zong_zi_chan >= zongjia:
    print("恭喜你购买成功")
else:
    print("你的余额不足，请充值")