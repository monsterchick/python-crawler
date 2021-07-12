import requests
from lxml import etree

url = 'https://www.996ak.com/mv/fs'

r = requests.get(url).content.decode('utf-8')
# 最左边的是tag，tag里面的是attribute， 两个包着的是text
title = etree.HTML(r).xpath('//h2[@class="entry-title"]/a/@title')
img = etree.HTML(r).xpath('//h2[@class="entry-title"]/a/@href')
print(title)
print(img)
