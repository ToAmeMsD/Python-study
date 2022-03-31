"""
#Author:ToSeeAll
#Date:2022/3/31
#GitHub:github.com/ToSeeAll
"""
# 该网站第一次会要求输入1，记录cookie才能进行后续访问
import json
import os
import random
import re
import string
import time

import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


# 才发现这玩意是用的图床https://search.pstatic.net/common?src=https://i.imgur.com/8rBB8lt.jpg
# 原始地址的图大，但是被墙了，前面这个也快了。。。


def check_cookie():
    newtime = int(time.time())
    # **************json读取************
    with open('cookies.json', 'r', encoding='UTF-8') as f:
        cookies = json.load(f)  # json格式数据
        cookies = json.loads(cookies)  # 字典格式数据
        bool = cookies.get('time')
        if bool:  # 是否存在时间这个索引
            oldtime = int(cookies.get('time'))
            # **************json写入*****************
            if newtime - oldtime > 86272:  # 24小时过期
                cookies = get_cookie()
                times = {'time': str(newtime)}
                cookies.update(times)  # 更新时间
                json_data = json.dumps(cookies)
                with open('cookies.json', 'w', encoding='utf-8') as f:
                    json.dump(json_data, f)
        else:
            cookies = get_cookie()
            times = {'time': str(newtime)}
            cookies.update(times)  # 更新时间
            json_data = json.dumps(cookies)
            with open('cookies.json', 'w', encoding='utf-8') as f:
                json.dump(json_data, f)
        return cookies


def get_cookie():
    """获取访问cookie，有效期大概24h"""
    # todo 2022/3/31 把cookies写入文件，以时间命名，获取当前时间，与cookies文件名比较，如果没超过24小时，则不获取cookies直接用
    _url = 'https://nsfwp.buzz/6653.html'
    browser = webdriver.Edge()
    browser.get(_url)
    browser.find_element(by=By.XPATH, value='//*[@id="acpwd-6653"]/form/input[1]').send_keys('1')
    browser.find_element(by=By.XPATH, value='//*[@id="acpwd-6653"]/form/input[2]').click()
    _cookies = browser.get_cookies()
    browser.close()
    my_cookie = {}
    for item in _cookies:
        my_cookie[item['name']] = item['value']
    return my_cookie


def get_pic_link(url, cookie):
    """输入画廊链接提取链接,元组"""
    # todo 2022/3/31 好像有两种显示方式，这是第一种
    txt = get_source(url, cookie)
    _links = re.findall(r'<figure class="wp-block-image"><img src="(.*?)" alt=""/></figure>', txt)
    if len(_links) == 0:
        _links = re.findall(r'<figure class="wp-block-image".*?<img src="(.*?)"', txt)
    return _links


def get_max_page(url):
    """获取首页最大页数,int"""
    txt = requests.get(url).text
    page = re.findall(r'"page-numbers" href="https://nsfwp.buzz/page/.*?">(.*?)</a>', txt)
    return max(page)


def file_download(_links):
    """传递一个链接数组，下载该数组的所有文件"""
    names = []
    print(_links)
    mytime = time.strftime('%Y-%m-%d-%H-%M', time.localtime())
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 4))  # 引入随机字符，防止覆盖
    save_path = mytime + '/' + ran_str
    _dir = os.listdir('.')
    if mytime in _dir:
        os.makedirs(save_path)
    else:
        os.makedirs(save_path)
    leng = len(_links)
    length = int(leng / 10) + 2
    for i in range(1, leng):
        names.append(save_path + '/' + (str(i).rjust(length, '0')) + '.jpg')  # 保存的文件名
    print('下载开始咯')
    # todo 2022/3/31 速度很慢，待添加多线程下载
    try:
        for _link, name in zip(_links, names):
            _res = requests.get(url=_link)
            f = open(name, 'wb')
            f.write(_res.content)
            f.close()
        print('好耶，下完了一个画廊')
    except Exception as e:
        print('出错了，错误原因：' + str(e))


def get_gallery(begin_page=0, stop_page=get_max_page('https://nsfwp.buzz/page/1')):
    """返回值好像是嵌套的元组，[page1的画廊['画廊1','画廊2'],page2的['','']]"""
    mylinks = []
    for page in range(begin_page, stop_page):
        url = 'https://nsfwp.buzz/page/' + str(page)  # 这里用来获取画廊
        txt = requests.get(url).text
        _links = re.findall(r'<a class="entry-image" href="(.*?)">', txt)
        mylinks.append(_links)
    return mylinks


def get_source(url, _my_cookie):
    """根据url和cookies获取源码"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55'
    }
    return requests.get(url, headers=headers, cookies=_my_cookie).text  # 带cookies获取画廊源码


if __name__ == '__main__':
    cookies = check_cookie()  # 获取cookies
    linktest = get_pic_link('http://nsfwp.buzz/6673.html', cookies)
    galleries = get_gallery(0, 5)  # 获取每一页的画廊
    print(galleries)
    for links in galleries:  # 此时的links指这一页的所有画廊
        for link in links:  # 此时的link指单个画廊链接
            mylink = get_pic_link(link, cookies)  # 获取这个画廊中的所有图片链接
            print(mylink)
            file_download(mylink)  # 下载图片
# todo 2022/3/31 麻了，网址墙了
