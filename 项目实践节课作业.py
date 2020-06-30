import random
import string
import pymongo


def create(datatype, range_, num, strlen=8):

        if datatype is str:
            for i in range(num):
                xm = ''.join(random.SystemRandom().choice(range_) for _ in range(strlen))
                yield xm

        elif datatype is int:
            for i in range(num):
                it = iter(range_)
                xm = random.randint(next(it), next(it))
                yield xm

        elif datatype is float:
            for i in range(num):
                it = iter(range_)
                xm = random.uniform(next(it), next(it))
                yield xm


def main():

    kh = pymongo.MongoClient("mongodb://localhost:38467/")
    db = kh["minghuiDB"]

    dblist = kh.list_database_names()
    if 'minghuiDB' in dblist:
        print('数据库已存在')
    print('\n')

    # 创建集合
    col = db["sites"]
    col.drop()

    str_ = create(str, string.ascii_letters, 50)
    int_ = create(int, [0, 100], 20)
    float_ = create(float, [0, 100], 20)

    for dict_str in str_:
        col.insert_one({'data': dict_str, 'datatype': 'str'})
    for dict_int in int_:
        col.insert_one({'data': dict_int, 'datatype': 'int'})
    for dict_float in float_:
        col.insert_one({'data': dict_float, 'datatype': 'float'})



    print('数据：')
    for x in col.find():
        print(x)
    print('\n')

    print('筛选')
    for i in col.find({"data": {"$regex": 'a'}, "type": "str"}):
        print(i)
    print('\n')

    print('筛选:')
    for i in col.find({"data": {"$gte": 10, "$lte": 50}, "type": "int"}):
        print(i)
    print('\n')

    print('筛选:')
    for i in col.find({"data": {"$gte": 10, "$lte": 50}, "type": "float"}):
        print(i)
    print('\n')



main()