# /usr/bin
# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
res = requests.get('http://news.sina.com.cn/china')
res.encoding = 'utf-8'
html_sample = '\
 <html> \
   <body> \
   <h1 id="title">Hello World</h1>\
   <a href="#" class="link">This is link1</a> \
   <a href="# link2" class="link">This is link2</a> \
   </body> \
 </html>'
soup = BeautifulSoup(html_sample,'lxml')
header = soup.select('#title')
print(header[0])
alink = soup.select('a')
print(alink)

for link in alink:
    #print(link)
    print(link['href'])
