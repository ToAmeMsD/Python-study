# switch语句

from __future__ import division

x = 1
y = 2
operator = input('请输入符号：')
result = {
    '+': x + y,
    '-': x - y,
    '*': x * y,
    '/': x / y
}
print(result.get(operator))


# 定义switch类
class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        yield self.match  # 返回一个生成器
        raise StopIteration  # 判断for循环是否结束

    def match(self, *args):
        if self.fall or not args:  # 模拟case子句
            return True
        elif self.value in args:  # 匹配成功
            self.fall = True
            return True
        else:  # 匹配失败
            return False


x = 1
y = 2
operator = input('请输入符号：')
for case in switch(operator):
    if case('+'):
        print(x + y)
        break
    if case('-'):
        print(x - y)
        break
    if case('*'):
        print(x * y)
        break
    if case('/'):
        print(x / y)
        break
    if case():
        print()
