"""
#Author:ToSeeAll
#Date:2022/3/31
#GitHub:github.com/ToSeeAll
"""
import re

import requests


# gallery" data-caption="" href="https://search.pstatic.net/common?src=https://i.imgur.com/sVElZ4D.jpg#vwid
def get_gallery(page):
    """获取画廊链接"""
    url = 'https://kkoo.icu/page/' + str(page)
    _res = requests.get(url).text
    # print(_res)
    _galleries = re.findall(r' <script>VOID_Ui.MasonryCtrler.watch.*?masonry-item.*?href="(.*?)">', _res, re.S)
    return _galleries


def get_pic_link(url):
    """获取画廊中的图片链接，返回link元组"""
    _res = requests.get(url).text
    _links = re.findall('gallery" data-caption="" href="(.*?)#vwid', _res)
    print(_links)
    return _links


if __name__ == '__main__':
    # 老站点，内容有点陈旧，新站点见pixcc
    # res = requests.get('https://kkoo.icu')
    # print(res.text)
    galleries = get_gallery(2)
    print(galleries)
    for link in galleries:
        get_pic_link(link)
# todo 2022/3/31 可以 ，等会弄
