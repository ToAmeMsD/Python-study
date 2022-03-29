"""
#Author:ToSeeAll
#Date:2022/3/29
#GitHub:github.com/ToSeeAll
"""
import os
from time import sleep

from selenium import webdriver
import edgedriver_autoinstaller

edgedriver_autoinstaller.install()
browser =webdriver.Edge(executable_path="msedgedriver.exe")
browser.get('https://madouqu.cc')
data=browser.page_source
print(data)
browser.quit()