# -*- coding: utf-8 -*
"""
根据输入的温度进行转换
"""
import re
TempStr = input("请输入带有符号的温度值:")
if re.match(r"^F|f", TempStr) or re.search(r"F|f$", TempStr):
    C = (eval(re.sub(r'\D', "", TempStr)) - 32)/1.8
    print("转换后的温度是{:.2f}C".format(C))
elif [re.match(r"^C|c", TempStr), re.search(r"$C|c", TempStr)]:
    F = 1.8*eval(re.sub(r'\D', "", TempStr))+32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("您输入的温度有误")