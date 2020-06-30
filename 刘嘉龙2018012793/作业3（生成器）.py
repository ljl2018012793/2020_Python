
import sys
import random

def fibonacci():  # 生成器函数 - 斐波那契
    for i in range(5):
        L1 = random.randint(1, 10)
        yield L1


f = fibonacci()  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f),end = ' ')
    except StopIteration:
        sys.exit()