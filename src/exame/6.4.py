"""
#Author:Tiany
#Date:2022/3/23
#Email:tianyu159357@gmail.com
"""
import re


def ex1():
    """存在字符串“I，love，python”，取出love并输出"""
    str = "I，love，python"
    print(str[2:6])
    print((str.split('，'))[1])  # 截取


def ex2():
    """存在字符串“aabbccddee”，将dd替换为ff。"""
    str = 'aabbccddee'
    print(str.replace('dd', 'ff'))


def ex3():
    """
    存在字符串“ab2b3n5n2n67mm4n2”，编程实现下面要求：
    1）使用re取出字符串中所有的数字，并组合成一个新的字符串输出。
    2）统计字符串中字母n出现的次数。
    3）统计每个字符出现的次数，使用字典输出，如{‘a’：1，’b’：2}。
    """
    "**********题1***********"
    str = 'ab2b3n5n2n67mm4n2'
    num = re.findall(r'\d', str)
    num = "".join(num)
    print(num, type(num))
    """***********题2*****************"""
    count = len(re.findall(r'n', str))
    print(count)
    "*********题3*******"
    mydict = {}
    for i in str:
        if i not in mydict.keys():  # 如果字符不在字典中，则新建一项
            mydict[i] = 1
        else:  # 字符在字典中，只需要数量加一
            mydict[i] += 1
    print(mydict)


if __name__ == '__main__':
    # ex1()
    # ex2()
    ex3()
