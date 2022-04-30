#!/usr/bin/env python3

import urllib
from bs4 import BeautifulSoup

httpResponse = urllib.request.urlopen("http://securitytube.net/video/3000")

html=htmlResponse.read()
bs = BeautifulSoup(html,'lxml')
print (bs.find('div' , id='labels'))

allLinks = descr.find_all('a')
print (allLinks)
videoLink = bs.find('iframe', {'title':'YouTube video player'})

print(videoLink['src'])
