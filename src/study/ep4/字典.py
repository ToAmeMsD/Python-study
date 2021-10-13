import sys

dict1 = {'a': 1, 'b': 2, 'c': 3}
print(type(dict1))
print(dict1)
print(dict1['a'])
print('%a,%(z)a,%(x)a' % {"z": "zzz", "x": "xxxx"})
dict1['d'] = 666
print(dict1)
for k in dict1:
    print('dict[%s]' % k, dict1[k])
print(dict1.items())
for (a, b) in dict1.items():
    print('dict[%s]' % a, b)
print(dict1.keys())
print(dict1.values())
# 浅拷贝
print("##########################")
dict12 = {'d': 23, 'c': 12}
dict12 = dict1.copy()
print(dict1, '\n', dict12)
dict1['a'] = 43
print(dict1, '\n', dict12)
dict12['b'] = 333
print(dict1, '\n', dict12)

# 全局字典
print(sys.modules.keys())
print(sys.modules.values())
print(sys.modules["os"])
