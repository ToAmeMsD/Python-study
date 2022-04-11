"""
#Author:ToSeeAll
#Date:2022/4/3
#GitHub:github.com/ToSeeAll
"""
import re

import requests


# fixme 2022/4/3 不好用
def getGalleries(url, rule, flag=None):
    """
    获取画廊链接\n
    :param url: 页面地址，字符串
    :param rule: 正则表达式规则
    :param flag: 是否匹配换行中的内容
    :return galleries: 返回画廊链接元组
    """
    res = requests.get(url).text
    if flag:
        galleries = re.findall(rule, res)
    else:
        galleries = re.findall(rule, res, re.S)
    return galleries


def getLinks(url, rule, flag=None):
    """
    获取画廊中的图片地址链接\n
    :param url: 画廊地址，字符串
    :param rule: 正则表达式规则
    :param flag: 是否匹配换行中的内容
    :return links: 返回画廊中所有图片链接元组
    """
    res = requests.get(url).text
    if not flag:
        links = re.findall(rule, res, re.S)
    else:
        links = re.findall(rule, res)
    return links
