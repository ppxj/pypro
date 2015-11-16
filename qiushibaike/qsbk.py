#-*-coding:utf8-*-
import requests
import re
# import sys
# reload(sys)
# sys.setdefaultencoding("gb18030")
# type=sys.getfilesystemencoding()
# http://www.qiushibaike.com/textnew/page/2?s=4823216  最新文字糗事
# http://www.qiushibaike.com/text/page/2?s=4823216 	 最热文字糗事
old_url='http://www.qiushibaike.com/textnew/page/2?s=4823782'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
html=requests.get('http://www.qiushibaike.com/textnew/page/2?s=4823213',headers=headers).content
# print html
title=re.findall('class="content">(.*?)<!--',html,re.S)
# print title
for each in title:
    print each
