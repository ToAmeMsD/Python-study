for x in range(-10, 10):
    if x > 0:
        print('正数', x)
    elif x == 0:
        print('零', x)
    else:
        print('负数', x)
else:
    print("循环结束")

for x in range(-1,10,1):
    if x == 6:
        print('找好了',x)
        break
    else:
        print(x)
