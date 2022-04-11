"""
#Author:ToSeeAll
#Date:2022/4/10
#GitHub:github.com/ToSeeAll
"""
import os
import re

import requests
# from fake_useragent import UserAgent

for page in range(1,15):
    # ua = UserAgent().random
    # print(ua)
    # headers = {
    #     'UserAgent': ua
    # }
    # proxy = {'http': 'http://192.168.1.107:20171'}
    url = 'https://www.bbnainai.com/tupian/page/'+str(page)
    res = requests.get(url).text
    # print(res)
    galleries = re.findall(r'''<a
            href="(.*?)"
            target="_blank"''', res, re.S)
    # print(galleries)
    for gallery in galleries:
        # gallery = galleries[0]
        res2 = requests.get(gallery).text
        # print(res2)
        links = re.findall(r'<img loading="lazy" width=".*?" height=".*?" src="(.*?)"', res2)
        title = ((re.findall(r'<title>(.*?)</title>', res2))[0]).replace(' ', '').replace('.', '-')
        # print(links)
        if len(links) > 0:
            for link in links:
                # subprocess.run(['/home/u145099/.local/bin/you-get','-o','meinvtui/'+title,link])
                name = link.split('/')[-1]
                save_path = 'bbnainai' + '/' + title
                _dir = os.listdir('bbnainai/')
                if title in _dir:
                    pass
                else:
                    os.makedirs(save_path)
                try:
                    _res = requests.get(link)
                    f = open(save_path + '/' + name, 'wb')
                    f.write(_res.content)
                    f.close()
                except Exception as e:
                    print('出错了，错误原因：' + str(e))
        else:
            print('empty links')
    print('page:', page)
