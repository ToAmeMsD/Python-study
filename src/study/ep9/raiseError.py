"""
#Author:ToSeeAll
#Date:2022/4/20
#GitHub:github.com/ToSeeAll
"""
"""手动抛出异常，一般用于抛出自定义异常"""
try:
    s = None
    if s is None:
        print('s 是空对象')
        raise NameError
    print(len(s))
except TypeError:
    print('空对象没有长度')
