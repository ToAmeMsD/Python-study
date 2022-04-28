"""
#Author:ToSeeAll
#Date:2022/4/26
#GitHub:github.com/ToSeeAll
"""
# https://233.fi/images/2017/06/27/90734b71fb0ec016b21cec38e505344c.md.jpg
import http.client

connect = http.client.HTTPConnection('https://233.fi:443')
connect.request('GET', '/images/2017/06/27/90734b71fb0ec016b21cec38e505344c.md.jpg')
res = connect.getresponse()
print(res.status, res.reason)
with open('1.jpg', 'wb') as f:
    f.write(res.read())
