#encoding:utf8
import requests
# from lxml import etree
# from multiprocessing.dummy import Pool
# html=requests.get('http://tieba.baidu.com/f?kw=python&fr=wwwt').content
# header('Mozilla/5.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/600.1.3 (KHTML, like Gecko) Version/8.0 Mobile/12A4345d Safari/600.1.4')
# print html;
# cook={"Cookie":"wp-settings-1=hidetb%3D1; wp-settings-time-1=1446099769; wordpress_test_cookie=WP+Cookie+check; bdshare_firstime=1445308866785; CNZZDATA1253215772=836093690-1446108941-http%253A%252F%252Flocalhost%252F%7C1446108941; CNZZDATA1256596510=300921649-1445675138-http%253A%252F%252Flocalhost%252F%7C1446281954"}
# url="http://localhost/wordpress/wp-admin/nav-menus.php"
# html=requests.get(url).content
# print html
# raw_input();
html=requests.get('https://login.weibo.cn/login/?ns=1&revalid=2&backURL=http%3A%2F%2Fweibo.cn%2F&backTitle=%CE%A2%B2%A9&vt=')
print html.content