import requests
import re
import time
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

f = open('C:/Users/Leisure/Desktop/doupo.txt','a+')

def get_info(url):
    res = requests.get(url,headers=headers)
    if res.status_code == 200:
        contents = re.findall('<p>(.*?)</p>',res.content.decode('utf-8'),re.S)
        for content in contents:
            f.write(content+'\n')
    else:
        pass
if __name__ == '__main__':
    urls = ['https://doupocangqiong1.com/1/{}.html'.format(str(i)) for i in range(1,3)]
    for url in urls:
        get_info(url)
        time.sleep(1)
f.close()