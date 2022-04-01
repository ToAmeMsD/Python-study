"""
#Author:ToSeeAll
#Date:2022/3/31
#GitHub:github.com/ToSeeAll
"""
import re

import requests

import FileDownload


# <div class="nv-post-thumbnail-wrap"><a href="https://everia.club/2022/04/01/risa-yukihira-%e9%9b%aa%e5%b9%b3%e8%8e%89%e5%b7%a6-flash%e3%82%b9%e3%83%9a%e3%82%b7%e3%83%a3%e3%83%ab%e3%82%b0%e3%83%a9%e3%83%93%e3%82%a2best-2022%e5%b9%b4%e6%96%b0%e5%b9%b4%e5%8f%b7/" rel="bookmark" title="Risa Yukihira 雪平莉左, FLASHスペシャルグラビアBEST 2022年新年号"><img fifu-featured="1" width="413" height="620" src="https://rakuda.my.id/wp-content/uploads/2022/03/0000-160.jpg" class="skip-lazy wp-post-image" alt="" title="" title="" /></a></div><h2 class="blog-entry-title entry-title"><a href="https://everia.club/2022/04/01/risa-yukihira-%e9%9b%aa%e5%b9%b3%e8%8e%89%e5%b7%a6-flash%e3%82%b9%e3%83%9a%e3%82%b7%e3%83%a3%e3%83%ab%e3%82%b0%e3%83%a9%e3%83%93%e3%82%a2best-2022%e5%b9%b4%e6%96%b0%e5%b9%b4%e5%8f%b7/" rel="bookmark">Risa Yukihira 雪平莉左, FLASHスペシャルグラビアBEST 2022年新年号</a></h2> </div>
def get_gallery(page):
    """获取画廊链接"""
    # url = 'https://everia.club/?paged=' + str(page)
    # 地区地址？不知道能不能用，测试一下
    url = 'https://everia.club/category/korea/page/' + str(page)
    _res = requests.get(url).text
    # print(_res)
    _galleries = re.findall(r'<div class="nv-post-thumbnail-wrap"><a href="(.*?)/"', _res, re.S)
    return _galleries


def get_pic_link(url):
    """获取画廊中的图片链接，返回字典{'title':xxx,‘links’：link元组}"""
    picInfo = {}
    _res = requests.get(url).text
    _links = re.findall('class="wp-block-image.*?src="(.*?)"', _res)
    _title = re.findall(r"""<meta name="twitter:title" content='(.*?)' />""", _res)
    picInfo['title'] = _title[0]
    picInfo['links'] = _links
    # print(picInfo)
    return picInfo


if __name__ == '__main__':
    # res = requests.get('https://everia.club')
    # print(res.text)
    galleries = get_gallery(1)
    # print(galleries)
    for gallery in galleries:
        mylinks = get_pic_link(gallery)
        if mylinks['links'] and mylinks['title']:
            FileDownload.download_with(mylinks)
            # print(mylinks)
# 第一页爬完了
# 地区界面只需要改url即可
# korea page2
