"""
#Author:ToSeeAll
#Date:2022/4/9
#GitHub:github.com/ToSeeAll
"""
import re
import subprocess
import requests

# https://mvtui.com/category/cos/page/5
# for page in range(1,2):
if __name__ == '__main__':
    url = 'https://mvtui.com/category/cos'  # +str(page)
    res = requests.get(url).text
    # print(res)
    galleries = re.findall(r'<div class="img"><a href="(.*?)" title=".*?" target="" rel="bookmark">', res)
    # print(galleries)
    for url in galleries:
        # url = galleries[0]#+str(page)
        res = requests.get(url).text
        # print(res)
        title = ((re.findall(r'<title>(.*?)</title>', res))[0]).replace(' ', '')
        links = re.findall(r'<img width="100%" src="(.*?)" data-src', res)
        # print(links)
        if len(links) > 0:
            for link in links:
                subprocess.run(['/home/u145099/.local/bin/you-get', '-o', 'meinvtui/' + title, link])
