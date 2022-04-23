"""
#Author:ToSeeAll
#Date:2022/4/21
#GitHub:github.com/ToSeeAll
"""
import os

if __name__ == '__main__':
    files = os.listdir('./')
    files = [x for x in files if os.path.isdir(x)]
    for _dir in files:
        htmlFiles = os.listdir(_dir)
        htmlFile = ['<a href="' + _dir + '/' + x + '">' + x.split('.')[0] + '</a>\n' for x in htmlFiles if '.html' in x]
        with open(_dir + '.html', 'w') as f:
            info = """<!DOCTYPE html>\n<html lang="en">\n<head>\n\t<meta charset="UTF-8">\n\t<title>""" + _dir + """</title>\n</head>\n<body>\n"""
            f.write(info)
            f.writelines(htmlFile)
            f.write('</body>\n</html>')
