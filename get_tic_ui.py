# -*- coding: utf-8 -*-
"""
ui
注意修改标签label时要用var.set()
Created by Charles-Deng
17jldeng@stu.edu.cn
"""

import tkinter as tk  # 使用Tkinter前需要先导入
import main_part

# 出票函数
def get_tic(discount_sta):
    # print(discount_sta)
    global tickets_dic
    global var5
    temp_list = main_part.get_tic(tickets_dic,discount_sta)
    try:
        # 设定折扣力度文本
        var5.set(temp_list[2])
        var2.set(temp_list[0])
        var3.set(temp_list[1])
    except:
        var2.set("无此折扣券！")
        var3.set("请重新尝试！")
# 滑条反馈绑定变量
def printScale(text):
    global discount_sta
    discount_sta = var4.get()

# 获取字典
global tickets_dic
tickets_dic = main_part.get_code_dic()
# 折扣选择状态
discount_sta = 0
# 主函数窗口
window = tk.Tk()
window.title('获取优惠券系统')
window.geometry('480x280')  # 这里的乘是小x
var1 = tk.StringVar()
# 设定顶标签
l0 = tk.Label(window, text="获取优惠券系统",bg = "brown", font=('Arial', 16), width=70, height=2)
l0.pack()
l00 = tk.Label(window, textvariable=var1, bg='brown',fg='white', font=('Arial', 12), width=70, height=2)

# 出券窗口
var2 = tk.StringVar()
var3 = tk.StringVar()
l1 = tk.Label(window, text="优惠券号：",font=('Arial', 12), width=10, height=2)
l2 = tk.Label(window, text="验证码：", font=('Arial', 12), width=10, height=2)
l3 = tk.Label(window, textvariable=var2, font=('Arial', 12), width=10, height=2)
l4 = tk.Label(window, textvariable=var3, font=('Arial', 12), width=10, height=2)

# 按钮和选择条窗口
global var4
# 用于绑定滑条变量
var4 = tk.StringVar()
s = tk.Scale(window, label='折扣选择条（0随机折扣）', from_=0, to=9, orient=tk.HORIZONTAL,
             length=200, showvalue=0,tickinterval=1, resolution=1,variable=var4,command=printScale)

b = tk.Button(window, text='获取', font=('Arial', 12), width=10, height=1, command=lambda :get_tic(discount_sta))
global var5
var5 = tk.StringVar()
var5.set("")
l5 = tk.Label(window, text="折扣力度：",font=('Arial', 12), width=10, height=2)
l6 = tk.Label(window, textvariable=var5,font=('Arial', 12), width=10, height=2)

l1.place(x=80, y=110, anchor='nw')
l2.place(x=80, y=150, anchor='nw')
l3.place(x=180, y=110, anchor='nw')
l4.place(x=180, y=150, anchor='nw')
l5.place(x=80, y=190, anchor='nw')
l6.place(x=180, y=190, anchor='nw')
b.place(x=180, y=230, anchor='nw')
s.pack()
window.mainloop()