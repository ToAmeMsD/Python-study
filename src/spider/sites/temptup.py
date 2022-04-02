"""
#Author:ToSeeAll
#Date:2022/3/29
#GitHub:github.com/ToSeeAll
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options

# todo 2022/3/31 才发现这玩意收费，弃了
def write_file(path, info):
    f = open(path, 'a+', encoding='UTF-8')
    for line in info:
        f.write(line + '\n')
    f.close()


def get_source(url):
    option = Options()
    option.add_argument('--proxy-server= http://192.168.1.107:20171')
    driver = webdriver.Edge(options=option)
    driver.get(url)
    return driver.page_source


if __name__ == '__main__':
    url = 'https://www.temptup.com'
    # res = get_source(url)
    option = Options()
    option.add_argument('--proxy-server= http://192.168.1.107:20171')
    driver = webdriver.Edge(options=option)
    driver.get(url)
    driver.find_element(by=By.XPATH, value='//*[@id="root"]/div[1]/div/div[1]/div[1]/div[2]').click()  # 跳转到登陆界面
    time.sleep(2)
    driver.find_element(by=By.XPATH,value='//*[@id="email"]').send_keys('cunhua1122@lista.cc')
    driver.find_element(by=By.XPATH,value='//*[@id="password"]').send_keys('cunhua1122')
    driver.find_element(by=By.XPATH, value='//*[@id="root"]/div[1]/div/div[2]/form/button').click()
    time.sleep(2)
    res = driver.page_source
    print(res)
