"""
#Author:ToSeeAll
#Date:2022/3/29
#GitHub:github.com/ToSeeAll
"""


class Fruits:
    """这是一个文档"""
    price = 0.0  # 类属性

    pass

    def __init__(self):
        self.color = 'red'  # 实例属性
        zone = 'china'  # 局部变量
        __a = ''


if __name__ == '__main__':
    print(Fruits.price)
    apple = Fruits()
    print(apple.color)
    apple.price = 10.2
    print(apple.price, apple.color)
    # print(apple.zone)  # 无法调用局部变量
    # print(apple._Fruits__a)  # 私有属性访问方式1
    print(apple.__doc__)
