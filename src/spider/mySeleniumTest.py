"""
#Author:ToSeeAll
#Date:2022/3/29
#GitHub:github.com/ToSeeAll
"""

# edgedriver_autoinstaller.install()
# browser =webdriver.Edge(executable_path="msedgedriver.exe")
# browser.get('https://madouqu.cc')
# # data=browser.page_source
# # print(data)
# # browser.quit()
import edgedriver_autoinstaller
from selenium import webdriver

edgedriver_autoinstaller.install()
browser = webdriver.Edge(executable_path="msedgedriver.exe")
browser.get('https://cn.bing.com/')
# *******************XPath定位***************
# browser.find_element_by_xpath('//*[@id="sb_form_q"]').send_keys('java')
# browser.find_element_by_xpath('//*[@id="search_icon"]').click()
# ********************CSS定位*****************
browser.find_element_by_css_selector('#sb_form_q').send_keys('c#')
browser.find_element_by_css_selector('#search_icon').click()
# ****************无界面浏览器**************

edgedriver_autoinstaller.install()
option = webdriver.ChromeOptions()
option.add_argument('--headless')
browser = webdriver.Edge(executable_path="msedgedriver.exe", Options=option)
