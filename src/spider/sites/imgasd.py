"""
#Author:ToSeeAll
#Date:2022/4/5
#GitHub:github.com/ToSeeAll
"""
import re

import requests

from spider.utils import CreateHtml

if __name__ == '__main__':
    # 韩国写真？
    for page in range(1, 57):
        url = 'https://imgasd.com/page/' + str(page)
        # https://imgasd.com/page/2
        res = requests.get(url)
        # print(res.text)
        galleries = re.findall(r'<figcaption><a href="(.*?)">.*?</a></figcaption>', res.text)
        galleries = ['https://imgasd.com' + x for x in galleries]
        # print(galleries)
        for gallery in galleries:
            res2 = requests.get(gallery).text
            link = re.findall(r'<img src="(.*?)">', res2)
            links = ['https://imgasd.com' + x for x in link]
            # print(links)
            CreateHtml.create_html(links, 'imgasd', page)
