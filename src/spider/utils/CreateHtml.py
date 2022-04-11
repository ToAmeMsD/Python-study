"""
#Author:ToSeeAll
#Date:2022/4/3
#GitHub:github.com/ToSeeAll
"""
import os.path


def create_html(_links, _dir, _page):
    """
    创建html文件，适用于国内网络可以访问的一般资源（好东西当然得存起来:)\n
    默认指在spider/目录下的相对路径，等写完了html再改\n
    :param _links: 图片链接，元组
    :param _dir: 保存目录，字符串
    :param _page: 页数
    :return:
    """
    # todo 2022/4/3 写好html项目后修改相对路径
    # fixme 2022/4/5 html文件缺少末尾，不过好像不影响
    # 相对目录指调用该函数的文件的相对目录
    if os.path.exists('C:/Users/Tiany/Documents/PyCharm/MyPythonStudy/src/spider/src/' + _dir):
        pass
    else:
        os.makedirs('C:/Users/Tiany/Documents/PyCharm/MyPythonStudy/src/spider/src/' + _dir)
    if os.path.exists('C:/Users/Tiany/Documents/PyCharm/MyPythonStudy/src/spider/src/' + _dir + '/' + _dir + str(_page) + '.html'):
        pass
    else:
        model = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"/>
    <title>瀑布流-multi-column</title>
    <style>
        .container {
            width: 100%;
            padding: 1px;
            border: 1px;
            column-count: 4;
            column-gap: 1px;
            column-width: 220px;
        }

        .img-container {
            margin-bottom: 1px;
            break-inside: avoid;
        }

        img {
            width: 100%;
        }
    </style>
</head>
<body>
<div class="container">\n"""
        with open('C:/Users/Tiany/Documents/PyCharm/MyPythonStudy/src/spider/src/' + _dir + '/' + _dir + str(_page) + '.html', 'a+', encoding='utf-8') as f:
            f.write(model)
    for src in _links:
        html = '<div class="img-container"><img src=" ' + src + ' " alt="" ></div>\n'
        with open('C:/Users/Tiany/Documents/PyCharm/MyPythonStudy/src/spider/src/' + _dir + '/' + _dir + str(_page) + '.html', 'a+', encoding='utf-8') as f:
            f.write(html)
    print('finished:', _page)
