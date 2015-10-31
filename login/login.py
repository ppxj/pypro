#-*-coding:utf8-*-
import requests
# from lxml import etree
# from multiprocessing.dummy import Pool
cook={"Cookie":""}
url="http://www.baidu.com"
html=requests.get(url).content
print html
raw_input();