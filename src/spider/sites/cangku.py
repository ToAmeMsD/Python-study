"""
#Author:ToSeeAll
#Date:2022/3/30
#GitHub:github.com/ToSeeAll
"""
import time
import requests
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By


def get_Cookie(url):
    browser = webdriver.Edge()
    browser.get(url)
    time.sleep(20)
    cookie = browser.get_cookies()
    browser.close()
    return cookie


class Cangku:
    def __init__(self):
        # todo 2022/3/30 麻了，这个网站用requests库获取不到源码
        print()


if __name__ == '__main__':
    url = 'https://cangku.icu/login'
    # print(get_Cookie(url))
    cookies = [
        {'domain': 'cangku.icu', 'expiry': 1648633143, 'httpOnly': True, 'name': 'cangku_laravel_session', 'path': '/',
         'secure': False,
         'value': 'eyJpdiI6ImxKaXV6U1VWVDNaOExwcTNTaThPWEE9PSIsInZhbHVlIjoiaW42bFRaT0JuT3VVdlcxR0V0bzU2UDN5d0NQSGg3N1NLRmpmK0Rla0s5THZKeHp4VDlBQmZHU3p1UStJS2tQYiIsIm1hYyI6IjZlMWEyOWJmYWM3MzY1MDNjYTU1ZDMyN2U2NTE0YjkxNmY5YTQ0YjQwNGViMDVjYWY3YjdhNTI4NGZlMDYyZDkifQ%3D%3D'},
        {'domain': 'cangku.icu', 'expiry': 1648633143, 'httpOnly': False, 'name': 'XSRF-TOKEN', 'path': '/',
         'secure': False,
         'value': 'eyJpdiI6IjBCYzhid2xEXC9jcjRHK29Bd3ZKYmdRPT0iLCJ2YWx1ZSI6InZTZWt2VzdGYXEzUlJMc0JOWmx5SUdcL2IxTjBuRDN2dDR4UVZpQnFlUWtQRDFpd0NES1Y2TnR1RSt5a1gxZFJqIiwibWFjIjoiNDJkZmMwYzYzYzhmZDVjY2JlNjc1ZDI1OWNiNjY3N2JkNzViMTE0ZTMyY2RhZjMxYzU1OTk3ZWZhMjU2MWRmMiJ9'},
        {'domain': 'cangku.icu', 'expiry': 1806305943, 'httpOnly': True,
         'name': 'remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d', 'path': '/', 'secure': False,
         'value': 'eyJpdiI6InVpbEk4R041U3pJUDVLZ2NnckM4VWc9PSIsInZhbHVlIjoiOGlQK0c4Nkx4OU9manRiYktCZURoMkpMUmNcL3ZHeDhLQm1DekNWWXd3NkFHa1BBcVpVcUs4QlF0VVVCR2JCXC9YYzlcL1pOWkZRdjlwelNDXC9CTmpZYkNtTlVVSTZ4Y0NreU1vTjUxTWZzNDNjUmpTQlwvdnA5SkF3Tmhpdko3bVF2WGpHWVZEejVubm9KYmVHZTdpSms2QzMwTldqR0liZzUzaDNUcjFJVHltck10RzhqNWJmTkZISHZwS0JIU0dlRnQiLCJtYWMiOiI3ZmQ1NDZiM2YyZGQ0MmYyZWIzNmJmN2JjMzBkZTI4YWNjMWY5NDYyMTVlMTE4ZThhM2ViYjlmYTljNGYxZmU2In0%3D'},
        {'domain': '.cangku.icu', 'expiry': 1711697929, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
         'value': 'GA1.2.226427880.1648625930'},
        {'domain': '.cangku.icu', 'expiry': 1648625989, 'httpOnly': False, 'name': '_gat_gtag_UA_103402143_1',
         'path': '/', 'secure': False, 'value': '1'},
        {'domain': '.cangku.icu', 'expiry': 1648712329, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
         'value': 'GA1.2.717655308.1648625930'},
        {'domain': 'cangku.icu', 'expiry': 1648627729, 'httpOnly': False, 'name': '_pk_ses.5.5493', 'path': '/',
         'sameSite': 'Lax', 'secure': False, 'value': '1'},
        {'domain': 'cangku.icu', 'expiry': 1682581129, 'httpOnly': False, 'name': '_pk_id.5.5493', 'path': '/',
         'sameSite': 'Lax', 'secure': False, 'value': 'efe4b538a8fde70b.1648625929.'}]

    # *********************request库**********
    # my_cookie = {}
    # for item in cookies:
    #     my_cookie[item['name']] = item['value']
    # print(my_cookie)
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55'
    # }
    # res=requests.get(url,headers=headers).text
    # print(res)

    # **********************selenium库*******
    # options = Options()
    # options.add_argument("headless")
    # driver = webdriver.Edge(options=options)
    driver=webdriver.Chrome()
    driver.get(url)
    driver.find_element(by=By.XPATH,value='//*[@id="login"]/div/form/div[3]/input').send_keys('3839126')
    driver.find_element(by=By.XPATH, value='//*[@id="login"]/div/form/div[4]/input').send_keys('qwer159357')
    driver.find_element(by=By.XPATH,value=r'//*[@id="login"]/div/form/button').click()
    time.sleep(2)
    driver.get('https://cangku.icu/category/59?page=1')
    res=driver.page_source
    # res = driver.page_source
    print(res)
