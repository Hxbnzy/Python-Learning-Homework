# -*- coding: utf-8 -*
a = input()
n = 6
s = 0
arr = []
while n > 0:
    n = n - 1
    s = float(a) * s
    if s == 0:
      s = 1
    arr.append(str(s))
print (' '.join(arr))