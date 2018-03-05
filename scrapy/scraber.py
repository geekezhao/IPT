# -*- coding: utf-8 -*-

__author__ = 'Zhao'

from bs4 import BeautifulSoup
import requests

sName = "new.txt"
f = open(sName, 'w+')

for i in range(1,188):
    url = "http://www.zju.edu.cn/xw/list" + str(i) + ".htm"
    
    headers = {
        'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",

    }
    r = requests.get(url, headers=headers)
    r.encoding='utf-8'
    demo = r.text
    soup = BeautifulSoup(demo,'html.parser')
    # print("**********************")

    for result in soup.find_all("ul", "news"):
        m=result.get_text()
        # print(m)
        f.write(m)
    print(url)


f.close()
