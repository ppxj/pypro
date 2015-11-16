#encoding:utf8
import requests
import re
# headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
# html=requests.get('http://www.qiushibaike.com/',headers=headers).content
# # print html.content
secret_code='at35q24tcfxxixx54fftxxlovexx345246xxyouxx46fgq'
# content=re.findall('x',html)
# print content

#.使用
# a='xy123'
# b=re.findall('x...',a)
# print b

#*的使用
# a='xyxy123'
# b=re.findall('x*',a)
# print b

# ?的使用
# a='xy123'
# b=re.findall('x?',a)
# print b

#.*使用
b=re.findall('xx.*xx',secret_code)
print b
# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")
# type=sys.getfilesystemencoding()