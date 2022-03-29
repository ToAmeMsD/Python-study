"""
#Author:ToSeeAll
#Date:2022/3/29
#GitHub:github.com/ToSeeAll
"""
import re

import requests


class LinkInfo:
    """测试用的类"""

    def __init__(self):
        self.date = ''
        self.link = ''


def get_source(path):
    """requests方式获取源码"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55'
    }
    html = requests.get(path, headers=headers).text
    return html


def get_gallery(txt):
    """返回某一页的全部画廊"""
    p = re.compile('<h2 class="entry-title"><a(.*?)">')
    _res = p.findall(txt)
    _gallery = {}
    for _info in _res:
        _res = _info.split('"')
        _gallery[_res[5]] = _res[3]
    return _gallery


def get_date(txt):
    """获取发布时间"""
    p = re.compile('<time datetime="(.*?)">')
    date = p.findall(txt)
    return date


def get_link(txt):
    """获取下载磁力链接"""
    p = re.compile('下載地址：<a href="(.*?)" rel=')
    link = p.findall(txt)
    return link


def test():
    # todo 2022/3/29 返回的数据有问题，是嵌套的元组，不需要嵌套，待修复
    mylinks = []
    _url = 'https://madouqu.cc'
    _res = get_source(_url)
    _gallery = get_gallery(_res)
    # print(_gallery)
    _url = [_gallery[i] for i in _gallery.keys()]  # 画廊的url
    for link in _url:
        txt = get_source(link)
        mylinks.append(get_link(txt))
    return mylinks


def write_file(path, info):
    f = open(path, 'a+', encoding='UTF-8')
    for line in info:
        f.write(line + '\n')
    f.close()


if __name__ == '__main__':
    # url = 'https://madouqu.cc'
    # res = get_source(url)
    # gallery = get_gallery(res)
    # print(gallery)
    #
    # url = [gallery[i] for i in gallery.keys()]  # 画廊的url
    # print(url)
    # links = LinkInfo()
    # res2 = get_source(url[0])  # 进入画廊
    # links.date = get_date(res2)  # 发布时间
    # links.link = get_link(res2)  # 磁链
    mylink = test()
    # write_file('links.txt', mylink)
    print(mylink)
