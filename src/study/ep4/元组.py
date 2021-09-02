def tup(tuple1):
    print('**************************************')
    print(tuple1)
    print(tuple1[0])
    print(type(tuple1))
    print(type(tuple1[0]))
    print(type('apple'))
    print(tuple1[-1])
    print(tuple1[-2])


def tup2(tup):
    tp = tup[0:3]
    return tp


if __name__ == '__main__':
    tuple1 = ('apple', 'faff', 'faraway', 'dada', 'kkkk')  # 元组打包
    tup(tuple1)
    print(tup2(tuple1))
    tuple2 = ((tuple1,), (tup2(tuple1),))
    print('**************************************')
    print(type(tuple2))
    print(tuple2)
    print(tuple2[1])
    print(tuple2[1][0])
    print(tuple2[1][0][1])
    print(tuple2[1][0][1][0])
    # print(tuple2[2][0][1])越界访问
    a, b, c, d, e = tuple2[0][0]  # 元组解包
    print(a, b, c, d, e)
    print('**************************************')
    for i in range(len(tuple1)):
        print('tuple1[%d]:' % i, end='')
        for j in range(len(tuple1[i])):
            print(tuple1[i][j], end='')
        print()
