"""
#Author:ToSeeAll
#Date:2022/3/29
#GitHub:github.com/ToSeeAll
"""

"""文件test.txt中包含以下内容：
    今年是2019年。
    2019年你好。
    2019年再见。
 1）读取该文件，并输出所有内容。
 2）去掉文件内容中的换行。
 3）计算出文件的长度。
 4）使用欧冠2020替换2019。
 5）创建另一个文件test2.txt，写入本文件的内容"""


def _1(pa):
    f = open(pa, 'r', encoding='utf-8')
    info = f.read()
    print(info)
    f.close()


def _2(pa, old, new):
    f = open(pa, 'r+', encoding='utf-8')
    pre = f.read()
    f.close()
    pre = pre.replace(old, new)
    f = open(pa, 'w', encoding='utf8')
    f.write(pre)
    f.close()


def _3(pa):
    f = open(pa, 'r', encoding='utf-8')
    f.read()
    print(f.tell())
    f.close()


def _4(path):
    _2(path, '2019', '欧冠2019')


def _5(pa,pa2):
    f = open(pa, 'r', encoding='utf-8')
    o = open(pa2, 'w', encoding='utf-8')
    txt = f.read()
    o.write(txt)
    f.close()
    o.close()




if __name__ == '__main__':
    path = 'test.txt'
    # _1(path)
    # _2(path,'\n','')
    # _3(path)# utf-8编码中中文占3个字节
    # _4(path)
    _5(path,'test2.txt')