import time

from bs4 import BeautifulSoup

import myRequestsTest


def bs_getInfo(url):
    """通过BeautifulSoup获取页面中所以画廊的标题和链接"""
    source = myRequestsTest.get_source(url)
    soup = BeautifulSoup(source, 'html.parser', exclude_encodings='utf-8')
    return soup.select('h2 a')


if __name__ == '__main__':
    # url = 'https://madouqu.cc'
    for page in range(0, 10):
        url = 'https://madouqu.cc/page/' + str(page)
        res = bs_getInfo(url)
        for info in res:
            print(info.text, info['href'])  # 包含标题与链接
        time.sleep(3)
    # link = soup.select('a')
    # print(link)
