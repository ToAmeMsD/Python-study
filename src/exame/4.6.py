from math import sqrt

# 对列表L[2,5,3,8,10,1]进行升序排序并输出
L = [2, 5, 3, 8, 10, 1]
L.sort()
print(L)

# 对给定的字符串‘123456’将其逆序输出，使用切片
s = '123456'
for i in range(len(s) - 1, -1, -1):
    print(s[i])
for j in range(-1, -len(s) - 1, -1):
    print(s[j])
print("*******************************")
# 对给定的字典d，输出其key和value，并插入新字典{'d':4},输出新字典
d = {'a': 1, 'b': 2, 'c': 3}
print(d.keys(), '  ', d.values(), "  ", "d[", d.keys(), "]", "=", d.values())
d['d'] = 4
print(d.keys(), '  ', d.values(), "  ", "d[", d.keys(), "]", "=", d.values())


# 求出100以内的所有素数，素数之间用逗号分隔

def is_prime(n):
    if n == 1:
        return False
    for _ in range(2, int(sqrt(n)) + 1):
        if n % _ == 0:
            return False
    return True


l1 = []
for i in range(1, 100):
    if is_prime(i):
        l1.append(i)
print(l1, len(l1))
