"""
#Author:ToSeeAll
#Date:2022/3/31
#GitHub:github.com/ToSeeAll
"""
import requests

if __name__ == '__main__':
    #老站点，内容有点陈旧，新站点见pixcc
    res = requests.get('https://kkoo.icu')
    print(res.text)
# todo 2022/3/31 可以 ，等会弄
