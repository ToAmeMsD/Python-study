"""
#Author:ToSeeAll
#Date:2022/3/30
#GitHub:github.com/ToSeeAll
"""
import re

import requests
from bs4 import BeautifulSoup


class Cunhua:
    def __init__(self):
        print()


def get_source(url):
    return requests.get(url).text


if __name__ == '__main__':
    url = 'https://www.cunhua.sbs'
    res = get_source(url)
    f = open('../src/cunhua.html', 'w', encoding='utf-8')
    f.write(res)
    f.close()
    soup = BeautifulSoup(res, 'html.parser', exclude_encodings='utf-8')
    select = soup.select('.img_big.cl a')
    # f = open('cunhua.txt', 'w', encoding='utf-8')
    # f.writelines(select)
    # f.close()
    # select = re.findall(r'<a href="((thread).*?(.*?))</a>',res)
    print(select)
