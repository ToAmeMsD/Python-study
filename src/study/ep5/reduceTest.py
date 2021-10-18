def func(x, y):
    return x * y


from functools import reduce

# 对序列中的元素进行连续操作
print(reduce(func, range(1, 10)))
print(reduce(func, range(1, 10), 10))
print(reduce(func, range(1, 1), 10))
