# 习题2.7
"""1. 以下变量命名不正确的是（　）。
A. foo=the_value
B. foo=1_value
C. foo=_value
D. foo=value_ &"""


def n1():
    the_value = 1
    # 1_value=12
    _value = 12
    # value_&=32
    foo = the_value
    # foo=1_value
    foo = _value
    # foo=value_&


# 2. 计算2的38次方的值。
def fff():
    i = 2
    j = 38
    print("2的38次方为：", i ** j)


"""3. 以下逻辑运算的结果：
a）True and False
b）False and True
c）True or False
d）False or True
e）True or False and True
f）True and False or False"""


def ddd():
    print("1：", True and False)
    print("2:", False and True)
    print("3:", True or False)
    print("4:", False or True)
    print("4:", True or False and True)
    print("5:", True and False or False)


# 4. 编写程序计算1+2+3+…+100的结果。
def ccc():
    sum = 0
    for i in range(1, 101):
        sum += i
    print(sum)


fff()
ccc()
ddd()
