"""
#Author:ToSeeAll
#Date:2022/4/2
#GitHub:github.com/ToSeeAll
"""
import re

import requests


def create_html(links):
    for src in links:
        html = '<img src="' + src + '">\n'
        with open('../src/LALA/img6.html', 'a+', encoding='utf-8') as f:
            f.write(html)


if __name__ == '__main__':
    # 爬完了
    links = ['https://233.fi/explore/?list=images&sort=title_asc&page=1',
             'https://233.fi/explore/?list=images&sort=title_asc&page=2&seek=005u7RWwly1fibkstpg4ij30ve2s019k.6d1T',
             'https://233.fi/explore/?list=images&sort=title_asc&page=3&seek=0064GroRgy1fgfwhtw8dbj30yi0jf765.oJGr',
             'https://233.fi/explore/?list=images&sort=title_asc&page=4&seek=006APx9Kgy1fji7a5tvbsj33k02dcb2e.6Ni3',
             'https://233.fi/explore/?list=images&sort=title_asc&page=5&seek=006APx9Kgy1fjp99a5081j30zk0qo45w.7yOI',
             'https://233.fi/explore/?list=images&sort=title_asc&page=6&seek=006FQh2Ygy1ffaeubautej316o1kwau6.2nu',
             'https://233.fi/explore/?list=images&sort=title_asc&page=7&seek=006FQh2Yly1fo5nbhs066j31401hc4bg.fV1K',
             'https://233.fi/explore/?list=images&sort=title_asc&page=8&seek=006H8TzLgy1ffogfiiv7nj32x12bcu0x.BC1H',
             'https://233.fi/explore/?list=images&sort=title_asc&page=9&seek=006joRgAly1fqiurzukb7j31400qotg9.P8lP',
             'https://233.fi/explore/?list=images&sort=title_asc&page=10&seek=006KLpBhly1ffqmqujyv1j30yi0n0afi.TT6',
             'https://233.fi/explore/?list=images&sort=title_asc&page=11&seek=006miUQrgy1ffvooi5bobj31e00xckgx.GJge',
             'https://233.fi/explore/?list=images&sort=title_asc&page=12&seek=006miUQrgy1fg3jzy23nkj30xc1e07t3.G2VX',
             'https://233.fi/explore/?list=images&sort=title_asc&page=13&seek=006miUQrgy1fgsspdz74mj30xc1e0ts5.GVaI',
             'https://233.fi/explore/?list=images&sort=title_asc&page=14&seek=006MRWCvgy1fr0ax5fagcj33vb2kxhdy.vH9T',
             'https://233.fi/explore/?list=images&sort=title_asc&page=15&seek=006MRWCvly1fr0bc46o4oj32kx3vbkjq.5eru',
             'https://233.fi/explore/?list=images&sort=title_asc&page=16&seek=006O3HnFly1fhkr8irh8dj30xc0m8gni.bRXK',
             'https://233.fi/explore/?list=images&sort=title_asc&page=17&seek=006T7KXEgy1fhm3bp4zkij31120oqdl5.bIXP',
             'https://233.fi/explore/?list=images&sort=title_asc&page=18&seek=12164895.1dM9',
             'https://233.fi/explore/?list=images&sort=title_asc&page=19&seek=12235868.ZxEX',
             'https://233.fi/explore/?list=images&sort=title_asc&page=20&seek=13083853.RQ9W',
             'https://233.fi/explore/?list=images&sort=title_asc&page=21&seek=17346656.RYlY',
             'https://233.fi/explore/?list=images&sort=title_asc&page=22&seek=17512776.cH2X',
             'https://233.fi/explore/?list=images&sort=title_asc&page=23&seek=17524957.eatS',
             'https://233.fi/explore/?list=images&sort=title_asc&page=24&seek=17535114.elcx',
             'https://233.fi/explore/?list=images&sort=title_asc&page=25&seek=17539725.msL4',
             'https://233.fi/explore/?list=images&sort=title_asc&page=26&seek=18916858.9Wvb',
             'https://233.fi/explore/?list=images&sort=title_asc&page=27&seek=19167977.mr78',
             'https://233.fi/explore/?list=images&sort=title_asc&page=28&seek=21333850.aZdG',
             'https://233.fi/explore/?list=images&sort=title_asc&page=29&seek=22515796.a35l',
             'https://233.fi/explore/?list=images&sort=title_asc&page=30&seek=25286518.y6iS',
             'https://233.fi/explore/?list=images&sort=title_asc&page=31&seek=25400364.fGZs',
             'https://233.fi/explore/?list=images&sort=title_asc&page=32&seek=26525705.IJKP',
             'https://233.fi/explore/?list=images&sort=title_asc&page=33&seek=26993680.IYxY',
             'https://233.fi/explore/?list=images&sort=title_asc&page=34&seek=26996907.9RjX',
             'https://233.fi/explore/?list=images&sort=title_asc&page=35&seek=26999683+%281%29.yWU1',
             'https://233.fi/explore/?list=images&sort=title_asc&page=36&seek=28358411.cBuY',
             'https://233.fi/explore/?list=images&sort=title_asc&page=37&seek=29148928.cn8H',
             'https://233.fi/explore/?list=images&sort=title_asc&page=38&seek=33459644.9AA3',
             'https://233.fi/explore/?list=images&sort=title_asc&page=39&seek=5dad5135gy1gpmrr06ls7j21o0280kjl.pS8y',
             'https://233.fi/explore/?list=images&sort=title_asc&page=40&seek=5dad5135gy1gqqa4qsb8vj23gg56okjx.peSP',
             'https://233.fi/explore/?list=images&sort=title_asc&page=41&seek=5dad5135gy1grfezzjrjqj231u4krqvh.ndQI',
             'https://233.fi/explore/?list=images&sort=title_asc&page=42&seek=5dad5135ly1fp96ij55s9j22472vi7wi.kEN3',
             'https://233.fi/explore/?list=images&sort=title_asc&page=43&seek=5dad5135ly1fpig5izf9fj22403607wm.kgBe',
             'https://233.fi/explore/?list=images&sort=title_asc&page=44&seek=5dad5135ly1fpma5kl5d5j2240360kjq.kjDb',
             'https://233.fi/explore/?list=images&sort=title_asc&page=45&seek=5dad5135ly1fpo1dx3kerj2240360npg.F0hI',
             'https://233.fi/explore/?list=images&sort=title_asc&page=46&seek=5dad5135ly1fpoq0nyf9yj20qo140tpn.xleP',
             'https://233.fi/explore/?list=images&sort=title_asc&page=47&seek=5dad5135ly1fqo2ucettqj2240360x6t.vcJG',
             'https://233.fi/explore/?list=images&sort=title_asc&page=48&seek=5dad5135ly1gk2xb01c6jj21yt1h44qq.pCrT',
             'https://233.fi/explore/?list=images&sort=title_asc&page=49&seek=5deb8c88gy1fqhgjtz8zpj21041044qp.Fl2x',
             'https://233.fi/explore/?list=images&sort=title_asc&page=50&seek=6632063923233624416.SIqD',
             'https://233.fi/explore/?list=images&sort=title_asc&page=51&seek=6e745b47gw1f496rmr0uvj21f01w0e84.4FtS',
             'https://233.fi/explore/?list=images&sort=title_asc&page=52&seek=6e745b47gw1f7eyof05mcj20lo0whwvx.0wV8',
             'https://233.fi/explore/?list=images&sort=title_asc&page=53&seek=6e745b47gy1fcoo54r1afj21e02301ky.4W5n',
             'https://233.fi/explore/?list=images&sort=title_asc&page=54&seek=6e745b47gy1fgf8h65410j21w02io1l1.ARoC',
             'https://233.fi/explore/?list=images&sort=title_asc&page=55&seek=6e745b47gy1fgidi7zzxdj21w02ionph.AOpX',
             'https://233.fi/explore/?list=images&sort=title_asc&page=56&seek=6e745b47gy1fhvc5jh3myj21400qoqbb.YR4r',
             'https://233.fi/explore/?list=images&sort=title_asc&page=57&seek=6e745b47gy1fleolwp4zcj21w02i1hdw.YzqW',
             'https://233.fi/explore/?list=images&sort=title_asc&page=58&seek=6e745b47gy1fof3b2u6rxj21w02io4qq.dkZy',
             'https://233.fi/explore/?list=images&sort=title_asc&page=59&seek=6e745b47ly1fp5tjf8fbaj21w02ioe81.5pvK',
             'https://233.fi/explore/?list=images&sort=title_asc&page=60&seek=6e745b47ly1fpxhs8jjm7j21w02iokjl.TZny',
             'https://233.fi/explore/?list=images&sort=title_asc&page=61&seek=6e745b47ly1fqo05070k9j21w02ioqv5.TOp3',
             'https://233.fi/explore/?list=images&sort=title_asc&page=62&seek=8729a648gy1fjzbvk478sj21f01w0kjo.ZVHW',
             'https://233.fi/explore/?list=images&sort=title_asc&page=63&seek=91fde477gy1fhcccxp78fj20qo140tfl.opPW',
             'https://233.fi/explore/?list=images&sort=title_asc&page=64&seek=9867f93bgy1fiwacnztxzj20qo0qowia.ok7M',
             'https://233.fi/explore/?list=images&sort=title_asc&page=65&seek=a93a9479gy1fk56xiu441j215o0rs1a3.VLIu',
             'https://233.fi/explore/?list=images&sort=title_asc&page=66&seek=aaf2c648gy1fjsazcrigzj21kw2dc7wh.849T',
             'https://233.fi/explore/?list=images&sort=title_asc&page=67&seek=bc413374gy1fi926k8lzxj215c1j41io.VNiX',
             'https://233.fi/explore/?list=images&sort=title_asc&page=68&seek=bc4833cegy1ffu69sc94yj20v90ku3zx.JAo3',
             'https://233.fi/explore/?list=images&sort=title_asc&page=69&seek=d949d336ly1fnrzspm13uj20qo0qognk.f0kl',
             'https://233.fi/explore/?list=images&sort=title_asc&page=70&seek=d949d336ly1fnv2s47qbwj21400qodip.sBeu',
             'https://233.fi/explore/?list=images&sort=title_asc&page=71&seek=e0cac6aagy1fhm8s0brczj20qo0zk10e.B9gX',
             'https://233.fi/explore/?list=images&sort=title_asc&page=72&seek=e8ef80a9gy1fhijmufaf3j21hc1z4tyt.BDlZ',
             'https://233.fi/explore/?list=images&sort=title_asc&page=73&seek=lala.im+2020+12+07+12+17+28.dW5l']
    for i in range(50, len(links)):
        res = requests.get(links[i]).text
        link = re.findall(r'<a href=".*?class="image-container --media">.*?<img src="(.*?)"', res, re.S)
        create_html(link)
        print(link)

# ****************************获取全部页面url
# url = 'https://233.fi/explore/?list=images&sort=title_asc&page=1'
# option = webdriver.ChromeOptions()
# prefs = {"profile.managed_default_content_settings.images": 2}  # 设置无图模式
# option.add_experimental_option("prefs", prefs)  # 加载无图模式设置
# option.add_argument("--headless")  # 设置无头模式
# browser = webdriver.Chrome(options=option)
# browser.get(url)
# # bool = browser.find_element(by=By.CSS_SELECTOR, value='#list-image-az-asc > ul > li.pagination-next')
# # print(bool)
# while True:
#     browser.find_element(by=By.CSS_SELECTOR, value='#list-image-az-asc > ul > li.pagination-next').click()
#     print(browser.current_url)
#     time.sleep(2)
