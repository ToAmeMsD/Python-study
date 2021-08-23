# 随机生成两个数，并比较其大小
import random


def compared(num1, num2):
    if num1 > num2:
        return num1
    elif num1 == num2:
        return 0
    else:
        return num2


def test():
    num1 = random.randrange(1, 100, 2)
    num2 = random.randrange(0, 99, 2)
    print("\n", num1)
    print("\n", num2)
    print("\n", compared(num1, num2))


test()
