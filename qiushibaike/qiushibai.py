#-*-coding:utf8-*-
import requests
import re
# import sys
# reload(sys)
# sys.setdefaultencoding("gb18030")
# type=sys.getfilesystemencoding()
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
html=requests.get('http://jp.tingroom.com/yuedu/yd300p',headers=headers).content
# print html
title=re.findall('style="color: #039;">(.*?)</a>',html,re.S)
# print title
for each in title:
    print each
