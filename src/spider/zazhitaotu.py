"""
#Author:ToSeeAll
#Date:2022/3/30
#GitHub:github.com/ToSeeAll
"""
import requests

if __name__ == '__main__':
    url = 'https://www.zazhitaotu.com'
    # url = 'http://icanhazip.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55'
    }
    http_proxy = {'http': 'http://127.0.0.1:12581'}
    res = requests.get(url, proxies=http_proxy, timeout=60, headers=headers).text
    print(res)
