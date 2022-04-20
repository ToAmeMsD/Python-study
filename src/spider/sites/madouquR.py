"""
#Author:ToSeeAll
#Date:2022/3/29
#GitHub:github.com/ToSeeAll
"""
import os.path
import re
import subprocess

import requests

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55'
    }
    url = 'https://madouqu.cc/'
    html = requests.get(url, headers=headers).text
    if os.path.exists('lastFile.txt'):
        with open('lastFile.txt', 'r') as f:
            tag = f.read()  # 记录最后一个
    else:
        tag = ''
    galleries = re.findall(r'<h2 class="entry-title"><a target="_blank" href="(.*?)"', html)
    for gallery in galleries:
        res = requests.get(gallery).text
        link = (re.findall(r'<p>下載地址：<a href="(.*?)" rel="follow" data-wpel-link="internal">Magnet', res)[0])  # 磁链
        check_tag = (gallery.split('/'))[-2]
        if check_tag == tag:
            break
        else:
            subprocess.run(['aria2c', link])
    with open('lastFile.txt', 'w') as f:
        f.write(((galleries[0].split('/'))[-2]))  # 把读到的第一个作为上次的最后一个保存
