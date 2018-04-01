# -*- coding: utf-8 -*
import re
'''
 货币转换
 人民币和美元间汇率固定为：1美元 = 6.78人民币
 人民币采用RMB表示，美元USD表示
'''
CyStr = input("请输入需要转换的货币:")
if re.search(r"^\d+(?:\.\d+)?RMB$|^RMB\d+(?:\.\d+)?$", CyStr):
    USD = eval(re.findall(r'\d+(?:\.\d+)?', CyStr)[0]) / 6.78
    print("USD" + '%.2f' % USD)
elif re.search(r"^\d+(?:\.\d+)?USD$|^USD\d+(?:\.\d+)?$", CyStr):
    RMB = 6.78 * eval(re.findall(r'\d+(?:\.\d+)?', CyStr)[0])
    print("RMB" + '%.2f' % RMB)
else:
    print("您输入的货币格式有误")


