"""
#Author:ToSeeAll
#Date:2022/4/3
#GitHub:github.com/ToSeeAll
"""
# https://www.bhhzw.com/page/12/
# 滚动翻页，实际网址如上
import re

import requests

from spider.utils import CreateHtml

if __name__ == '__main__':
    url = 'https://www.bhhzw.com/page/1/'
    res = requests.get(url).text
    galleries = re.findall(r'<a class="item-link" href="(.*?)">', res)
    # print(galleries)
    # <img class="post-item-img lazy" src="https://www.xxfoo.com/images/2021/06/12/20180916203725_90448.jpg" data-original="https://www.xxfoo.com/images/2021/06/12/20180916203725_90448.jpg" alt="韩国美女车模申海莉生活照写真笑容迷人 [3]" title="韩国美女车模申海莉生活照写真笑容迷人 [3]" style="">
    #
    res2 = requests.get(galleries[1]).text
    links = re.findall(r'<img class="post-item-img lazy" src=.*?data-original="(.*?)"', res2)
    # print(links)
    CreateHtml.create_html(links, 'bhhzw', 1)
