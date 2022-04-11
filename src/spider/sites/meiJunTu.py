"""
#Author:ToSeeAll
#Date:2022/4/3
#GitHub:github.com/ToSeeAll
"""
# https://meijuntu.com/tags/cosplay-2.html
# https://meijuntu.com/tags/cosplay-124.html
import re

import requests

from spider.utils import CreateHtml

'''
<li>
<a href="/beauty/wanghongcoserxiezhen_sally_dorasn76131.html" target="_blank">
<img src="https://i.wujituku.com/jmt/mm/2021112414/thumb_0_500_403gzs3cmsh.jpg" alt="[网红COSER写真] Sally Dorasnow - Super Crown Boo 套图">
<p>[网红COSER写真] Sally Dorasnow - Super Crown Boo 套图</p>
</a>
</li>
'''


# 套娃翻页，画廊中还得翻页
def paQu(_page):
    # 只爬100页，后边的欣赏不来。。。
    # ******************获取画廊*********
    url = 'https://meijuntu.com/tags/cosplay-' + str(_page) + '.html'
    res = requests.get(url).text
    galleries = re.findall(r'<a href="/b(.*?).html" target="_blank">', res)
    galleries = ['https://meijuntu.com/b' + g for g in galleries]
    for gallery in galleries:
        # ****************获取图片页数*********
        res2 = requests.get(gallery + '.html').text
        page = re.findall(r'''.html">(.*?)</a> <a class="a1" href=".*?">下一页</a>''', res2)
        page = page[0].split('>')[-1]
        print(page)
        # *********获取图片链接********************
        links = []
        for i in range(1, int(page) + 1):  # 套娃翻页，效率极低
            url = gallery + '-' + str(i) + '.html'  # 翻页地址
            # print(url)
            res = requests.get(url).text
            link = re.findall(r'''<div class="pictures">
<img src="(.*?)"''', res)
            # print(link)
            # *********************************
            links.append(link[0])  # 每页只有一张图
        # print('links:', links)
        CreateHtml.create_html(links, 'meiJunTu', _page)


if __name__ == '__main__':
    for i in range(1, 100):
        paQu(i)
