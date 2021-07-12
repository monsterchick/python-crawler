import requests
from lxml import etree

url = 'https://www.keaitupian.net/'

r = requests.get(url).content.decode('utf-8')
e = etree.HTML(r).xpath('//div[@class="items_likes"]/a[@href]/text()')
print(e)