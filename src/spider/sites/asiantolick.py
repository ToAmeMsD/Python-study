"""
#Author:ToSeeAll
#Date:2022/4/6
#GitHub:github.com/ToSeeAll
"""
# https://asiantolick.com/category-90/Lolita
# 其中之一，其它也可以看看
import re
import subprocess

import requests

for page in range(1, 38):
    url = 'https://asiantolick.com/ajax/buscar_posts.php?post=&cat=&tag=&search=&page=&index=' + str(
        page) + '&ver=29'  # 37页
    # url = 'https://asiantolick.com/ajax/buscar_posts.php?cat=90&index='+str(page)  # 8页
    res = requests.get(url).text
    # print(res)
    galleries = re.findall(r'<a mob="0" webp="0" href="(.*?)" target="" class="miniatura"', res)
    # print(galleries)  # 链接似乎直接以文件名加-转义后为url
    for gallery in galleries:
        res2 = requests.get(gallery).text
        imglinks = re.findall(r'<div data-src="(.*?)"', res2)
        imglinks = [x for x in imglinks if x[-3::] == 'jpg']
        videolinks = re.findall(r'<source src="(.*?)" type="video/mp4">', res2)
        videolinks = [x for x in videolinks if x[-3::] == 'mp4']  # 筛选视频
        if len(videolinks) > 0:
            for link in videolinks:
                subprocess.run(['/home/u149263/.local/bin/you-get', '-o', 'lolita/video', link])
        if len(imglinks) > 0:
            for link in imglinks:
                subprocess.run(['/home/u149263/.local/bin/you-get', '-o', 'lolita/img', link])
    print('done', page)
