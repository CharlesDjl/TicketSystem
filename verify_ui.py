# -*- coding: utf-8 -*-
"""
ui界面
注意修改标签label时要用var.set()
Created by Charles-Deng
17jldeng@stu.edu.cn
"""

import tkinter as tk  # 使用Tkinter前需要先导入
import main_part
import time

def verify():
    quanhao = str(e1.get())
    mima = str(e2.get())
    danhao = str(e3.get())
    jine = str(e4.get())
    main_part.check(quanhao, mima, danhao, jine, tickets_dic, var1)

def upgrade():
    global window2
    window2 = tk.Tk()
    window2.title('管理员系统')
    window2.geometry('300x180')  # 这里的乘是小x

    lx = tk.Label(window2, text="请输入管理员密码", bg="brown", font=('Arial', 16), width=50, height=2)
    lx.pack()
    ex = tk.Entry(window2, show="*", font=('Arial', 14))  # 显示成密文形式
    ex.pack()
    bx = tk.Button(window2, text='确认', font=('Arial', 12), width=10, height=1, command=lambda:confirm(ex))
    bx.pack()
def confirm(ex):
    code = str(ex.get())
    # 重建数据库所需管理员密码
    if code == "1234":
        # ly = tk.Label(window2, text="成功", font=('Arial', 16), width=50, height=2)
        get_new_dic()
        window2.destroy()
    else:
        ly = tk.Label(window2, text="失败", font=('Arial', 16), width=50, height=2)
        ly.pack()
def get_new_dic():
    # 根据设定获取新的数据库
    global window3
    window3 = tk.Tk()
    window3.title('管理员系统')
    window3.geometry('300x180')  # 这里的乘是小x
    lx = tk.Label(window3, text="请输入想创建的折扣券库", bg="brown", font=('Arial', 16), width=50, height=1)
    lx.pack()
    lx2 = tk.Label(window3, text="（0表示随机）", bg="brown", font=('Arial', 16), width=50, height=1)
    lx2.pack()
    ex = tk.Entry(window3, font=('Arial', 14))  # 显示成密文形式
    ex.pack()
    bx = tk.Button(window3, text='确认', font=('Arial', 12), width=10, height=1, command=lambda:new_dic_confirm(ex))
    bx.pack()
def new_dic_confirm(ex):
    discount = str(ex.get())
    main_part.create_code_dictionary(discount)
    ly = tk.Label(window3, text="成功", font=('Arial', 16), width=50, height=2)
    ly.pack()
# 主函数
def main_window():
    global tickets_dic
    tickets_dic = main_part.get_code_dic()
    window = tk.Tk()
    window.title('优惠券兑换系统')
    window.geometry('500x380')  # 这里的乘是小x
    global var1
    var1 = tk.StringVar()
    # 设置转换按钮
    # 设定输入标签
    l0 = tk.Label(window, text="优惠券兑换系统",bg = "brown", font=('Arial', 16), width=70, height=2)
    l0.pack()
    var1.set("")
    l00 = tk.Label(window, textvariable=var1, bg='brown',fg='white', font=('Arial', 12), width=70, height=2)

    l1 = tk.Label(window, text="优惠券号：",font=('Arial', 12), width=10, height=2)
    l2 = tk.Label(window, text="验证码：", font=('Arial', 12), width=10, height=2)
    l3 = tk.Label(window, text="消费单号：", font=('Arial', 12), width=10, height=2)
    l4 = tk.Label(window, text="金额：", font=('Arial', 12), width=10, height=2)
    # 设置输入窗口
    global e1,e2,e3,e4
    e1 = tk.Entry(window, show=None, font=('Arial', 14))  # 显示成明文形式
    e2 = tk.Entry(window, show=None, font=('Arial', 14))
    e3 = tk.Entry(window, show=None, font=('Arial', 14))
    e4 = tk.Entry(window, show=None, font=('Arial', 14))

    b = tk.Button(window, text='验证', font=('Arial', 12), width=10, height=1, command=verify)
    b2 = tk.Button(window, text='重置数据库', font=('Arial', 12), width=11, height=1, command=upgrade)
    l1.place(x=80, y=100, anchor='nw')
    e1.place(x=180, y=104, anchor='nw')
    l2.place(x=80, y=150, anchor='nw')
    e2.place(x=180, y=154, anchor='nw')
    l3.place(x=80, y=200, anchor='nw')
    e3.place(x=180, y=204, anchor='nw')
    l4.place(x=80, y=250, anchor='nw')
    e4.place(x=180, y=254, anchor='nw')
    b.place(x=100, y=300, anchor='nw')
    b2.place(x=280, y=300, anchor='nw')
    l00.pack()
    window.mainloop()
if __name__ == '__main__':
    main_window()