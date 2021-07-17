import requests
from lxml import etree


# get the lyrics
url = 'https://beckyxmaggie.pixnet.net/blog/post/344721071-eminem%E9%98%BF%E5%A7%86-love-the-way-you-lie-ft.-rihanna--%E4%B8%AD%E6%96%87%E6%AD%8C%E8%A9%9E'
response = requests.get(url).content
etree = etree.HTML(response).xpath('//p[@style="text-align: center;"]/span')

lyricsList = []
for eachLine in etree:
    # append all words into a list
    lyricsList.append(eachLine.text + '\n')

    # save the lyrics to local address
    path = r'C:\Users\Monster Chick\Desktop\save_lyrics\lyrics.txt'
    with open(path, 'w') as f:
        f.writelines(lyricsList)
    f.close()
print('done')

# for testing
print(lyricsList)
