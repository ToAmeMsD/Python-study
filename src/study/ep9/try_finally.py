"""
#Author:ToSeeAll
#Date:2022/4/20
#GitHub:github.com/ToSeeAll
"""
try:
    f = open('file.txt', 'r')
    try:
        print(f.read())
    except:
        print('读取错误')
    finally:
        print("释放资源")
        f.close()
except FileNotFoundError:
    print("文件不存在")
