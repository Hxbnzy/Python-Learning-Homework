# -*- coding: utf-8 -*
# 浮点与答案不相符
# 😡
import re
a = input()
n = 6
i = 0
arr = []
while n > 0:
    n = n - 1
    i = eval(a) * i
    if i == 0 and re.search(r"^[1-9]\d*$", a):
        i = 1
    elif i == 0:
        i = 1.0
    arr.append(str(i))
print (' '.join(arr))