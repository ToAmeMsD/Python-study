"""
#Author:ToSeeAll
#Date:2022/3/31
#GitHub:github.com/ToSeeAll
"""
import json

cookie = {'_ga_9K7CJ96FQ0': 'GS1.1.1648724049.1.1.1648724090.0', '_ga': 'GA1.1.1140190301.1648724050',
          'PHPSESSID': '809gji3g8ban5chc1vclpmu42a'}
# json_data = json.dumps(cookie)
# with open('cookies.json', 'w', encoding='utf-8') as f:
#     json.dump(json_data, f)
# with open('cookies1.json', 'r', encoding='utf-8') as f:
#     data = json.load(f)
#     print(data)
#     cookie = json.loads(data)
#     print(cookie)

time = {'time': '234'}
cookie.update(time)
print(cookie)
json_data = json.dumps(cookie)
with open('cookies.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f)