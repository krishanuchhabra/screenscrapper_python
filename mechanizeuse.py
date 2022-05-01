#!/usr/bin/env python3

import mechanize

br = mechanize.Browser() #creating a browser object
br.open('http://www.securitytube.net/video/3000')
for forms in br.forms():
    print (forms)

br.select_form(nr=0)
br.form['q']= 'defcon'
#fill the q parameter of the first form selected 

br.submit()

for links in br.links():
    print (links)

for links in br.links():
    print(links.url + ":" + links.ttext)
