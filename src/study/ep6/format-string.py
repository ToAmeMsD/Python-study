import operator
from functools import reduce


def main():
    """格式化字符串"""
    str1 = 'version'
    str2 = '''
    aaa #hhhh
    bbb
    '''
    str3 = """
    aaa # hhhh
    bbb    
    """
    num = 84924.32232
    print(str1)
    print(str2)
    print(str3)
    print(num)
    print('ni hao %s %d %.2f cai guai' % (str1, num, num))


def duiqi():
    """字符串对齐"""
    word = 'this is some words'
    print(word)  # 未对齐
    print(word.center(40))  # 以40个字符的长度中心对齐
    print(word.center(40, "*"))  # 以40个字符的长度中心对齐，以*号填充其余区域
    print(word.ljust(0))
    print(word.ljust(40, '#'))
    print(word.rjust(30, '*'))
    print(word.rjust(40))
    print('%20s' % word)


def zhuanyi():
    path = 'hello\npython'
    path2 = 'hello\tpython'
    path3 = r'hello\tpython\n'
    print('path:%s,path.len:%d \npath2:%s,path2.len:%d \npath3:%s,path3.len:%d' % (
        path, len(path), path2, len(path2), path3, len(path3)))
    path4 = 'hello\bpython'
    print(path4)


def hebing():
    str1 = 'hello'
    str2 = 'world'
    str3 = 'hhhh'
    result = str1 + str3
    print(result)
    result2 = '666'.join(result)  # 使用join会把字符串当成列表,且每次连接一次
    print(result2)
    result3 = ['ni', 'hao', 'ya']
    print(result3, '555'.join(result3))
    print(reduce(operator.add, result3, ''))


def jiequ():
    print()


if __name__ == '__main__':
    # main()
    # duiqi()
    # zhuanyi()
    hebing()
