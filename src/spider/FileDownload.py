"""
#Author:ToSeeAll
#Date:2022/4/1
#GitHub:github.com/ToSeeAll
"""
import asyncio
import os
import random
import string
import time

import aiohttp


async def job(session, url, name):
    """异步下载"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55'
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
        mytime = time.strftime('%Y-%m-%d-%H-%M', time.localtime())
        ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 4))  # 引入随机字符，防止覆盖
        save_path = mytime + '/' + ran_str
        _dir = os.listdir('.')
        if mytime in _dir:
            os.makedirs(save_path)
        else:
            os.makedirs(save_path)
        leng = len(url)
        length = int(len(str(leng))) + 1
        for i in range(0, leng):
            names.append(save_path + '/' + (str(i).rjust(length, '0')) + '.jpg')  # 保存的文件名
        tasks = [loop.create_task(job(session, url[_], names[_])) for _ in range(len(url))]
        finshed, unfinshed = await asyncio.wait(tasks)
        all_results = [r.result() for r in finshed]
        print('All Result:' + str(all_results))


async def main_with(loop, url, title):
    """带有标题传入的异步下载主函数"""
    async with aiohttp.ClientSession() as session:
        names = []
        mytime = time.strftime('%Y-%m-%d-%H-%M', time.localtime())
        ran_str = title
        save_path = mytime + '/' + ran_str
        _dir = os.listdir('.')
        if mytime in _dir:
            os.makedirs(save_path)
        else:
            os.makedirs(save_path)
        leng = len(url)
        length = int(len(str(leng))) + 1
        for i in range(0, leng):
            names.append(save_path + '/' + (str(i).rjust(length, '0')) + '.jpg')  # 保存的文件名
        tasks = [loop.create_task(job(session, url[_], names[_])) for _ in range(len(url))]
        finshed, unfinshed = await asyncio.wait(tasks)
        all_results = [r.result() for r in finshed]
        print('All Result:' + str(all_results))


def download_without(mylink):
    """没有标题的链接元组下载，按照时间创建文件夹"""
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop, mylink))


def download_with(mylinks):
    """带有标题的链接元组下载，按照时间创建文件夹"""
    title = mylinks['title']
    title = title.replace(' ', '-').replace('/', '-').replace('\\', '-').replace(':', '-').replace('.',
                                                                                                   '-').replace(
        '?', '-').replace('*', '-').replace(',', '-')
    mylink=mylinks['links']
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main_with(loop, mylink, title))
