# coding=utf-8
"""
 简单进度条
"""
import time
scale = 100
print("开始".center(scale//2, "-"))
start = time.perf_counter()
for i in range(scale + 1):
    a = (i/scale) * 100
    b = i * "*"
    c = (scale - i) * "."
    dur = time.perf_counter() - start
    print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(a, b, c, dur), end="")
    time.sleep(0.1)
print("\n"+"结束".center(scale//2, "-"))
