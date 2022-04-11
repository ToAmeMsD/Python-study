"""
#Author:ToSeeAll
#Date:2022/4/9
#GitHub:github.com/ToSeeAll
"""
import re

import requests
from fake_useragent import UserAgent

ua = UserAgent()
# 公共请求头
public_headers = {
    # 'cookie': '__cfduid=d3af1fe4e02395143768f49120192d89a1612161290; _gid=GA1.2.537470263.1612161292; shunt=1; AVS=pgucjspmo4rgafa4vinl3feug4; ipcountry=TW; ipm5=ad96616d894884f20b4e263448a05911; _ga_YYJWNTTJEN=GS1.1.1612339484.9.1.1612339785.59; _gat_ga0=1; _gat_ga1=1; _ga=GA1.2.2093487367.1612161292; _gat_gtag_UA_99252457_3=1; cover=1; _gali=chk_cover',
    'User-Agent': ua.random
}
if __name__ == '__main__':
    url = 'https://www.jav.ink/category/litu100/'
    res = requests.get(url).text
    # print(res)

    galleries = re.findall(r'<a href="https://www.jav.ink/litu100/(.*?)"> <img', res)
    # print(galleries)
    galleries = ['https://www.jav.ink/litu100/' + x for x in galleries]
    galleries = tuple(list(galleries))
    # print(galleries)

    for gallery in galleries:
        # gallery = galleries[0]
        res2 = requests.get(gallery).text
        # print(res2)
        links = re.findall(r'''<dt class='gallery-icon portrait'>
				<a href='(.*?)'>''', res2, re.S)
        # print(links)
