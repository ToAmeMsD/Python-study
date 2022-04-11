"""
#Author:ToSeeAll
#Date:2022/4/2
#GitHub:github.com/ToSeeAll
"""
import os.path
import re

import requests

from spider.utils import CreateHtml


def create_html(_links, _page):
    for src in _links:
        html = '<img src="' + src + '">\n'
        with open('../src/huaManLou/huaManLou' + _page + '.html', 'a+', encoding='utf-8') as f:
            f.write(html)


if __name__ == '__main__':
    # 52页
    dirs = '../src/huaMAnLou'
    if os.path.exists(dirs):
        pass
    else:
        os.makedirs(dirs)
    for page in range(1, 4):
        url = 'http://20887.net/tags-47_' + str(page) + '.html'
        # http://20887.net/tags-47_2.html
        res = requests.get(url).text
        galleries = re.findall(r'<div class="col-lg-3 col-md-3\s\scol-xs-6 mt20">.*?<a href="(.*?)"', res, re.S)
        # print(galleries)
        res2 = requests.get(galleries[0]).text
        links = re.findall(r'<img src="(.*?)jpg" alt=".*?">', res2)
        links = list(set(links))  # 转成列表以去重
        links = tuple(set(links))  # 还原成元组方便操作
        links = [link + 'jpg' for link in links]
        CreateHtml.create_html(links, 'huaManLou', page)
        # print(links)
# 第4页开始就废了，后边代码变了
