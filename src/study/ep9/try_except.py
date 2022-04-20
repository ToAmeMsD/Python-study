"""
#Author:ToSeeAll
#Date:2022/4/20
#GitHub:github.com/ToSeeAll
"""

while True:
    try:
        i = input('请输入除数:\t')
        i = int(i)
        a = 212 / i
    except ZeroDivisionError:
        print('数据异常，请检查输入。')
    except ValueError:
        print('输入类型异常，请确认。')
    else:
        print('结果为', a)
        break
