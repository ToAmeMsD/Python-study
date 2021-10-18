def func(x):
    if x % 5 == 0:
        return x


# 过滤序列，筛选出能被5整除的数字
print(filter(func, range(0, 101)))
print(list(filter(func, range(0, 101))))
