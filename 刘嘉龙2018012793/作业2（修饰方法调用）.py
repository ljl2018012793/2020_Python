# coding: utf-8
# @Author  : Liujl
# @FileName: 作业2（修饰方法调用）.py
# @Software: PyCharm
import random
import string

def MainData (type, value, num, strlen=10):
    try:
        key = set()
        if type is float:
            while True:
               temp = iter(value)
               count = random.uniform(next(temp), next(temp))
               key.add(count)
               if len(key) >= num:
                    break
        elif type is int:
            while True:
                temp = iter(value)
                count = random.randint(next(temp), next(temp))
                key.add(count)
                if len(key) >= num:
                    break
        elif type is str:
            while True:
               count = ''.join(random.SystemRandom().choice(value) for _ in range(strlen))
               key.add(count)
               if len(key) >= num:
                   break
    except Exception as end:
        print(end)
    else:
        return key
    finally:
        print('')
        print('')
        print(" 原始数据:")

def ChooseData (data, *key):
    try:
        result = set()
        for count in data:
            if type(count) is str:
                for son in key:
                    if son in count:
                        result.add(count)
            elif type(count) is int or type(count) is float:
                temp = iter(key)
                if next(temp) <= count <= next(temp):
                    result.add(count)
        return result
    except Exception as end:
        print(end)
    finally:
        print(f"筛选条件: {key}")
        print("筛选结果:")

def Dec1(Int):
    def modify1():
        Int()
    return modify1
@Dec1
def Int():
    result = MainData(int, [10, 50], 10)
    print(result)
    original = ChooseData(result, 20, 40)
    print((original) , end=' ')

def Dec2(Float):
    def modify2():
        Float()
    return modify2
@Dec2
def Float():
    result = MainData(float, [10, 50], 10)
    print(result)
    original = ChooseData(result, 20, 40)
    print((original), end='')

def Dec3(String):
    def modify3():
        String()
    return modify3
@Dec3
def String():
    base_str = string.ascii_letters+string.digits
    result = MainData(str, base_str, 100)
    print(result)
    original = ChooseData(result, 'a', 'b', 'c')
    print((original), end='')

Int()
Float()
String()