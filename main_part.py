"""
优惠券系统
Created by Charles-Deng
17jldeng@stu.edu.cn
"""
import random
import csv
import numpy as np
import pandas as pd
import time

path = "C:\\Users\\Charles\\Desktop\\tickets_access.csv"
# 输入为折扣力度，0默认随机，1-9为折扣。
def create_code_dictionary(discount_sta):
    # 券号密码位宽
    id_width = 8
    code_width = 6
    control_dic = {}
    # 生成优惠券的数量
    numbers = 1000
    for i in range(numbers):
        # 使用状态，获取状态，消费单号，消费金额，折扣后金额
        use_sta = 0
        get_sta = 0
        series_num = ""
        cost = ""
        discount_num = ""
        # sample(seq, n) 从序列seq中选择n个随机且独立的元素；
        id = ''.join(str(o) for o in random.sample(range(1,9),id_width))
        code = ''.join(chr((o)) for o in random.sample(range(97,122),code_width)) # 97-122对应小写字母
        if int(discount_sta) == 0:
            # 5~9折优惠券
            discount = random.randint(5,9)
        else:
            discount = int(discount_sta)
        control_dic[id] = [code,use_sta,series_num,cost,get_sta,discount,discount_num]
    dic_into_csv(control_dic)
def dic_into_csv(dic):
    csv_name = ["id", "code", "use_sta", "series_num", "cost","get_sta","discount","discount_num"]
    csv_data = zip(list(dic.keys()), [list(dic.values())[k][0] for k in range(len(dic))]
                   , [list(dic.values())[k][1] for k in range(len(dic))],
                   [list(dic.values())[k][2] for k in range(len(dic))],
                   [list(dic.values())[k][3] for k in range(len(dic))],
                   [list(dic.values())[k][4] for k in range(len(dic))],
                   [list(dic.values())[k][5] for k in range(len(dic))],
                   [list(dic.values())[k][6] for k in range(len(dic))])
    tickets_access = pd.DataFrame(columns=csv_name, data=csv_data)
    tickets_access.to_csv(path)
# 解析csv格式的密码本
def get_code_dic():
    with open(path, 'r') as f:
        reader = csv.reader(f)
        result = list(reader)
    tickets_dic = {}
    # 处理行信息
    for row in result:
        if row[0] == "":
            continue
        id_str = row[1]
        code_str = row[2]
        use_sta_str = row[3]
        sn_str = row[4]
        cost_str = row[5]
        get_sta_str = row[6]
        discount_str = row[7]
        discount_num_str = row[8]
        tickets_dic[id_str] = [code_str,int(use_sta_str),sn_str,cost_str,int(get_sta_str),
                               int(discount_str),discount_num_str]
    return tickets_dic
# 查验
def check(quanhao,mima,danhao,jine,tickets_dic,var1):
    danhao_list = [tickets_dic[key][2] for key in tickets_dic.keys()]
    # 检查优惠券是否被获取
    if tickets_dic[quanhao][4] == 1:
        if mima == tickets_dic[quanhao][0]:
            # 检查优惠券是否已被使用
            if tickets_dic[quanhao][1] != 0:
                print("该优惠券已被使用！")
                var1.set("该优惠券已被使用！")
            # 消费单号是否已记录
            elif danhao in danhao_list:
                print("该消费单已被记录！")
                var1.set("该消费单已被记录！")
            else:
                tickets_dic[quanhao][1] = 1
                tickets_dic[quanhao][2] = danhao
                tickets_dic[quanhao][3] = jine
                temp_dis = float(0.1*float(jine)*tickets_dic[quanhao][5])
                tickets_dic[quanhao][6] = round(temp_dis,1)
                dic_into_csv(tickets_dic)
                print("验证成功！")
                var1.set("验证成功！优惠后金额为："+str(tickets_dic[quanhao][6]))
        else:
            print("券号或密码不正确！")
            var1.set("券号或密码不正确！")
    else:
        var1.set("该优惠券尚未发出！")
# 获取优惠券
def get_tic(dic,discount_sta):
    if int(discount_sta) == 0: # 随机折扣出票
        for key in dic.keys():
            # 获取状态为0
            if dic[key][4] == 0:
                dic[key][4] = 1
                out = [key,dic[key][0],dic[key][5]]
                dic_into_csv(dic)
                return out
    else:
        for key in dic.keys():  # 指定折扣出票
            if dic[key][4] == 0 and dic[key][5] == int(discount_sta):
                dic[key][4] = 1
                out = [key,dic[key][0],dic[key][5]]
                dic_into_csv(dic)
                return out
if __name__ == '__main__':
    pass
    # begin_time = time.time()
    # create_code_dictionary(0)    # 创建/刷新密码本
    # tickets_dic = get_code_dic()  # 获取密码本
    # # output = get_tic(tickets_dic)
    # end_time = time.time()
    # print(end_time - begin_time)