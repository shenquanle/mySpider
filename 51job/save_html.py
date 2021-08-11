import csv
import time
from requests.adapters import HTTPAdapter
import requests
from lxml import etree
import random


original_urls = open('./后端开发.csv')
url_items = csv.reader(original_urls)

s = requests.Session()
s.mount('http://', HTTPAdapter(max_retries=3))
s.mount('https://', HTTPAdapter(max_retries=3))
header_judge = 0
for target_url in url_items:
    url = target_url[0]
    if not url.startswith('h'):
        continue
    header_judge += 1
    print(header_judge, url)

    if header_judge % 4 == 1:
        header = {
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'
                  }
    elif header_judge % 4 == 2:
        header = {
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
                  }
    elif header_judge % 4 == 3:
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    else:
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362"
        }
    try:
        res = s.get(url, headers=header, timeout=10)
        res.encoding = "gbk"
        html_content = res.text
        with open('./后端开发/'+ str(header_judge)+ '.txt', 'w') as f:
            f.writelines(html_content)
        print(type(html_content))
        time.sleep(random.randint(3,5))
    except Exception as e:
        print(e)
