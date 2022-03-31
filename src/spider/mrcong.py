"""
#Author:ToSeeAll
#Date:2022/3/31
#GitHub:github.com/ToSeeAll
"""
import requests

if __name__ == '__main__':
    res = requests.get('https://mrcong.com')
    print(res.text)
# todo 2022/3/31 可以，等会弄
