"""
#Author:ToSeeAll
#Date:2022/4/5
#GitHub:github.com/ToSeeAll
"""
import re

import requests

from spider.utils import CreateHtml

if __name__ == '__main__':
    for page in range(1, 84):
        url = 'https://www.yaomitao.com/jptt/page/' + str(page)  # 有三个分区，这是其中之一，83页
        res = requests.get(url).text
        galleries = re.findall(r'''<a target="_blank" href="(.*?)"><img class="lazyload"''', res)
        # print(galleries[0])
        for gallery in galleries:
            res2 = requests.get(gallery).text
            links = re.findall(
                r'''<img src="https://www\.yaomitao\.com/img.php\?url=(.*?)" alt=".*?" class="aligncenter">''', res2)
            CreateHtml.create_html(links, 'yaomitao', page)
