"""
#Author:ToSeeAll
#Date:2022/4/10
#GitHub:github.com/ToSeeAll
"""
import re

import requests

if __name__ == '__main__':
    url = 'https://sisterasian.com/?page=1'
    res = requests.get(url).text
    # print(res)
    galleries = re.findall(r'<a class="play-icon" href="(.*?)">', res)
    galleries = ['https://sisterasian.com/' + x for x in galleries]
    galleries=tuple(list(galleries))
    print(galleries)