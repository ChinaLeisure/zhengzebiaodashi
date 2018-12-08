import re
import requests
res = requests.get('http://bj.xiaozhu.com/')
prices = re.findall('<span class="result_price">&#165;<i>(.*?)</i>/晚 </span>',res.text)
for price in prices:
    print(price)