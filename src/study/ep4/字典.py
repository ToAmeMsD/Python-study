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
