# -*- coding: utf-8 -*
import re
'''
 根据输入的温度进行转换
 C表示摄氏度、F表示华氏度
 C = ( F - 32 ) / 1.8
 F = C * 1.8 + 32
'''
TempStr = input("请输入带有符号的温度值:")
if re.search(r"^\d+(?:\.\d+)?(F|f)$|^(F|f)\d+(?:\.\d+)?$", TempStr):
    C = (eval(re.findall(r'\d+(?:\.\d+)?', TempStr)[0]) - 32) / 1.8
    print("C" + '%.2f' % C)
elif re.search(r"^\d+(?:\.\d+)?(C|c)$|^(C|c)\d+(?:\.\d+)?$", TempStr):
    F = 1.8 * eval(re.findall(r'\d+(?:\.\d+)?', TempStr)[0]) + 32
    print("F" + '%.2f' % F)
else:
    print("您输入的温度有误")

