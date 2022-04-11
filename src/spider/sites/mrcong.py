"""
#Author:ToSeeAll
#Date:2022/3/31
#GitHub:github.com/ToSeeAll
"""
import re

import requests

# 进入画廊后的标题<title>[BlueCake] Yuka (유카): Secret Date (155 ảnh)</title>
# 画廊图片链接<img class="aligncenter" src="https://i2.wp.com/kul.mrcong.com/images/2022/03/30/BlueCake-Yuka-Secret-Date-MrCong.com-003.jpg?w=955&#038;ssl=1"
# 页面中所有的画廊<h2 class="post-box-title">
#			<a href="https://mrcong.com/xiuren-no-4226-zhou-yuxi-sandy-93-anh/
# https://mrcong.com/page/2/
from spider.utils import CreateHtml


def get_gallery(page):
    """获取画廊链接"""
    url = 'https://mrcong.com/page/' + str(page)
    _res = requests.get(url,timeout=30).text
    # print(_res)
    _galleries = re.findall(r'<h2 class="post-box-title".*?href="(.*?)/">', _res, re.S)
    return _galleries


def get_pic_link(url):
    """获取画廊中的图片链接，返回字典{'title':xxx,‘links’：link元组}"""
    picInfo = {}
    _res = requests.get(url,timeout=30).text
    _links = re.findall('<img class="aligncenter" src="(.*?)\?w=', _res)
    # _title = re.findall(r'<title>(.*?)</title>', _res)
    # picInfo['title'] = _title[0]
    # picInfo['links'] = _links
    # print(picInfo)
    return _links


if __name__ == '__main__':
    for page in range(23, 200):  # 800页
        galleries = get_gallery(page)
        # print(galleries)
        for url in galleries:
            links = get_pic_link(url)
            CreateHtml.create_html(links, 'mrcong', page)
