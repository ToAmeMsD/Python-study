# 通过map对元组进行解包

def func(x):
    return x ** x


def func2(x, y):
    return x ** y


print(map(func, range(1, 5)))
print(list(map(func, range(1, 5))))
print(map(func2, range(1, 5), range(5, 1, -1)))
print(list(map(func2, range(1, 5), range(5, 1, -1))))
