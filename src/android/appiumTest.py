"""
#Author:ToSeeAll
#Date:2022/3/31
#GitHub:github.com/ToSeeAll
"""
from appium import webdriver

desired_caps = {
    'newCommandTimeout': 3600,
    'platformName': 'Android',
    'deviceName': '192.168.1.103:43211',
    'platformVersion': '11', 'uuid': '192.168.1.103:43211', 'appPackage': 'com.tencent.mm',
    'appActivity': 'com.tencent.mm.ui.LauncherUI'

}
browser = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
size=browser.get_window_size()
print(size)