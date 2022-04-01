"""
#Author:ToSeeAll
#Date:2022/4/1
#GitHub:github.com/ToSeeAll
"""
# https://www.v2ph.com/country/china?page
# 写真，不漏点
import asyncio
import os
import random
import re
import string

import aiohttp
import requests


# <a class="media-cover" href="/album/IMISS-640">
# <img class="card-img-top" src="https://cdn.v2ph.com/album/GMMSfQmc_hdRd9Vk.jpg" data-src="https://cdn.v2ph.com/album/GMMSfQmc_hdRd9Vk.jpg" alt="[IMISS爱蜜社] VOL.640 小狐狸Kathryn 蕾丝诱惑小蛮腰" style="opacity: 1;">
# </a>
# 画廊里<div class="album-photo my-2" style="padding-bottom: 150%;"><img src="data:image/gif;base64,R0lGODdhAQABAPAAAMPDwwAAACwAAAAAAQABAAACAkQBADs=" data-src="https://cdn.v2ph.com/photos/pXSzHOzVq06NXpOl.jpg" class="img-fluid album-photo d-block mx-auto" alt="[IMISS爱蜜社] VOL.638 小狐狸Kathryn 丝袜 美臀 0"></div>
def get_gallery(page):
    """获取画廊链接"""
    url = 'https://www.v2ph.com/country/south-korea?page=' + str(page)
    _res = requests.get(url).text
    _galleries = re.findall(r'<a class="media-cover" href="(.*?)">', _res, re.S)
    _galleries = ['https://www.v2ph.com' + x for x in _galleries]
    return _galleries


def get_pic_link(url):
    """获取画廊中的图片链接，返回字典{'title':xxx,‘links’：link元组}"""
    # 这个网站有小页面，得翻页才能得到所有图片地址。。。。好了，没事了，得登录才能翻页，就爬一页吧
    # 返回值有重复，不过网站有VIP限制，懒得修了
    picInfo = {}
    _res = requests.get(url).text
    if '您需要登陆才能观赏该相册的内容' in _res:  # 这玩意有会员判定，有的画廊不能看
        return picInfo
    else:
        _links = re.findall('<div class="album-photo my-2".*?data-src="(.*?)"', _res)
        _title = re.findall(r'<title>(.*?)</title>', _res)
        _title = _title[0].replace('Eunji&#039;s ', '')
        _title = _title.replace(' ', '-').replace('/', '-').replace('\\', '-').replace(':', '-').replace('.',
                                                                                                         '-').replace(
            '?', '-').replace('*', '-')
        picInfo['title'] = _title
        picInfo['links'] = _links
        # print(picInfo)
        return picInfo


async def job(session, url, name):
    """异步下载"""
    headers = {
        'authority': 'cdn.v2ph.com',
        'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_gid=GA1.2.160286265.1648796793; fpestid=hPx5aD0tpKXRmd4mtGHRb5c-AoT53tmN4UN7nMM1OIsEaOI1TdmQg7nIO4jOPEnsYXkmag; __cf_bm=R8N8RrtwtL6EBxTnsz2rBMqRcn4jDjFDQ0zbe.kZMz8-1648798957-0-AXWwqm2U80N0AgFQmRZS6tzWaAhGyiiNVpSLI/U/m24W71wdcFiMbzJjErQLelvzAuG/HaLl5U6KGQ/xSzmT/wHr7Sfer11YzhSp9o6JUQ5Xtm1Piiw63kHc56fhjGyhnQ==; _gat_UA-140713725-1=1; _ga_170M3FX3HZ=GS1.1.1648796793.1.1.1648799025.32; _ga=GA1.2.1051232166.1648796793',
        'referer': 'https://www.v2ph.com/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'image',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36',
    }
    img = await session.get(url, headers=headers, timeout=120)
    imgcode = await img.read()
    with open(str(name), 'wb') as f:
        f.write(imgcode)
    return str(url)


async def main(loop, url):
    """异步下载主函数"""
    async with aiohttp.ClientSession() as session:
        names = []
        title = url['title']
        url = url['links']
        save_path = 'v2ph/south-korea/' + title
        _dir = os.listdir('.')
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        else:
            save_path = save_path + ''.join(
                random.sample(string.ascii_letters + string.digits, 2))  # 因为这代码得到的图集有重复的，所以得加个随机
            os.makedirs(save_path)
        leng = len(url)
        length = int(len(str(leng))) + 1
        for i in range(0, leng):
            names.append(save_path + '/' + (str(i).rjust(length, '0')) + '.jpg')  # 保存的文件名
        tasks = [loop.create_task(job(session, url[_], names[_])) for _ in range(len(url))]
        finshed, unfinshed = await asyncio.wait(tasks)
        all_results = [r.result() for r in finshed]
        print('All Result:' + str(all_results))


def yibu_download(mylink):
    """异步下载启动管理"""
    # *******多线程使用*****************
    # new_loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(new_loop)
    # ******************************
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop, mylink))


if __name__ == '__main__':
    # 下载需要添加header：
    # south-korea有30页
    # 30页下完了
    for page in range(1, 30):
        galleries = get_gallery(page)
        # print(galleries)
        for gallery in galleries:
            links = get_pic_link(gallery)
            if links != {}:
                yibu_download(links)
        print('当前页：', page)
