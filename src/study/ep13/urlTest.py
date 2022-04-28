"""
#Author:ToSeeAll
#Date:2022/4/26
#GitHub:github.com/ToSeeAll
"""
from urllib.parse import *
from urllib.request import urlopen, urlretrieve

url = urljoin('https://blog.toame.tk', 'index.html')
# print(url)
a = urlsplit(url)
print(a)
c = quote('编码')
print(c)
print(unquote(c))
a = urlopen('http://www.baidu.com')
with open('index.html', 'wb') as f:
    while True:
        b = a.read(1024)
        if not b:
            break
        f.write(b)
a.close()
d, m = urlretrieve('https://233.fi/images/2017/06/27/90734b71fb0ec016b21cec38e505344c.md.jpg','1.jpg')

