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
    # 相对目录指调用该函数的文件的相对目录
    if os.path.exists('./src/' + _dir):
        pass
    else:
        os.makedirs('./src/' + _dir)
    for src in _links:
        html = '<img src="' + src + '">\n'
        with open('./src/' + _dir + '/' + _dir + str(_page) + '.html', 'a+', encoding='utf-8') as f:
            f.write(html)
    print('all files is done')
