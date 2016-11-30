#-*-coding:utf-8-*-
#总调用文件
#Python 3.5.2 64-bit
import os
fin = open('temp','w')
fin.close()
import fwork
import checker
import swork
import open

print("本系统由唐瀚林（FSOL）制作，仅用于厦门大学管理层语料项目。\n使用python版本：Python 3.5.2 64-bit\n联系邮箱：tanghanlincpp@163.com\n\n")
x = input("输入0自动运行全套，输入指定数字运行指定阶段\n")
x = str(x)
if(x == '0'):
    fwork.work()
    checker.work()
    swork.work()
    open.work()
elif(x=='1'):
    fwork.work()
elif(x=='2'):
    checker.work()
elif(x=='3'):
    swork.work()
elif(x=='4'):
    open.work()
else:
    print("指令错误\n")

print("程序结束")
