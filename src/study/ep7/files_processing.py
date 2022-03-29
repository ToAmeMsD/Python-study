"""
#Author:ToSeeAll
#Date:2022/3/23
#GitHub:github.com/ToSeeAll
"""
# -*- coding: utf-8 -*-
import configparser
import os


def file_test():
    file = open('hello.txt', 'a+')
    file.write('hello world\n')
    print(file.tell())
    file.seek(0, 0)
    print(file.tell())
    f = file.read()
    print(f)
    file.close()


def splist():
    """获取指定目录下的文件，并分成元组"""
    files = os.listdir('.')
    print(len(files))
    for file in files:
        name = os.path.splitext(file)
        print(name)


def getIni():
    """读取ini配置文件"""
    config = configparser.ConfigParser()
    config.read('test.ini', encoding='UTF-8')
    section = config.sections()  # 读取所有配置块
    print(section)
    config_modul = config.options(section[0])  # 读取配置项
    print(config_modul)
    config_items = config.items(section[0])  # 配置项内容
    print(config_items)


def setIni():
    """修改ini配置文件"""
    config = configparser.ConfigParser()
    config.add_section('我就用中文')  # 添加配置块
    print(config.sections())
    "如果需要修改配置项，只需要先打开，再调用set设置即可"
    config.set(config.sections()[0], '这是配置项', '这是配置项的值')
    f = open('test.ini', 'a+', encoding='utf8')  # 以utf-8编码写入，不然中文乱码
    config.write(f)
    f.close()


def delIni():
    """配置文件ini相关删除"""
    config = configparser.ConfigParser()
    config.read('test.ini', encoding='utf8')
    "删除配置项"
    config.remove_option(config.sections()[-1], config.options(config.sections()[-1])[-1])
    config.remove_section(config.sections()[-1])
    f = open('test.ini', 'w+', encoding='utf8')
    config.write(f)
    f.close()


def dir_editor():
    os.mkdir('testdir')
    # os.mkdir('hellp/hhh')#mkdir,rmkdir一次只能创建(删除)一层文件夹
    os.makedirs('hellp/hhh')
    print(os.listdir('.'))


if __name__ == '__main__':
    # file_test()
    # splist()
    # getIni()
    # setIni()
    # delIni()
    dir_editor()
