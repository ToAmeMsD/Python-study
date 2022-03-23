import datetime
import operator
import re
import time
from functools import reduce


def geshihua():
    """格式化输出字符串"""
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
    """字符串转义"""
    path = 'hello\npython'
    path2 = 'hello\tpython'
    path3 = r'hello\tpython\n'
    print('path:%s,path.len:%d \npath2:%s,path2.len:%d \npath3:%s,path3.len:%d' % (
        path, len(path), path2, len(path2), path3, len(path3)))
    path4 = 'hello\bpython'
    print(path4)


def hebing():
    """字符串合并"""
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
    """字符串截取"""
    str = 'pattern Recognition:1,2,3,4,https://www.baidu.com'
    print("空格分割子串：", str.split())
    print("逗号分割子串：", str.split(','))
    print("逗号分割子串：", str.split(',', 2))
    print("斜杠分割子串：", str.split('/'))
    print("提取指定位置的文本：", str.split('/')[-1])


def bijiao():
    """字符串比较"""
    str1 = 1
    str2 = '1'
    if str1 == str2:
        print('相同')
    else:
        print('不同')
    if str(str1) == str2:
        print('相同')
        print(type(str2))
    else:
        print('不同')
    if str1 == int(str2):
        print('相同')
        print(type(str1))
    else:
        print('不同')


def fanzhuan():
    """字符串的反转"""
    out = ""
    str = '12345678'
    li = list(str)
    for i in range(len(li), 0, -1):
        out += ''.join(li[i - 1])
    print(str)
    print(out)
    print(str[::-1])  # 从最后一个开始索引


def foun_reduce():
    """字符串查找与替换"""
    # 查找字符串
    sentence = "This is a apple."
    print(sentence.find("a"))
    sentence = "This is a apple."
    print(sentence.rfind("a"))  # 10指的还是从前往后的序号

    # 字符串替换
    sentence = "hello world, hello China"
    print(sentence.replace('he', '66'))
    print(sentence)
    print(sentence.replace('1', 'k'))
    print(sentence)
    print(sentence.replace('hel', '77', 3))


def formattime():
    """字符串与日期的转换"""
    mytime = time.strftime('%Y年%m月%d日 %X', time.localtime())
    print(mytime)
    yourtime = time.strptime('2022年03月23日 15:05:20', '%Y年%m月%d日 %X')
    print(yourtime)
    y, m, d = yourtime[0:3]
    print(datetime.datetime(y, m, d))


def zhengguishi():
    """正则表达式"""
    s = 'HELLO WORLD'
    print(re.findall('^hello', s))
    print(re.findall('^hello', s, re.IGNORECASE))
    print(re.findall(r'^wo', s, re.IGNORECASE))
    print(re.findall(r'wORLD', s))
    print(re.findall(r'wORLD', s, re.IGNORECASE))
    print(re.findall(r'WORLD$', s, re.IGNORECASE))


if __name__ == '__main__':
    # main()
    # duiqi()
    # zhuanyi()
    # hebing()
    # jiequ()
    # bijiao()
    # fanzhuan()
    # foun_reduce()
    # formattime()
    zhengguishi()
