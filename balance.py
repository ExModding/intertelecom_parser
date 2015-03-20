#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import sys
from bs4 import BeautifulSoup

URL = 'https://assa.intertelecom.ua/ru/login'

### Enable this in case of insecure connection error ###
#requests.packages.urllib3.disable_warnings()

if len(sys.argv) <= 1:
    print('Error! Please specify login and password')
    sys.exit(1)

payload = {'phone': sys.argv[1], 'pass': sys.argv[2]}
page = requests.post(URL, data=payload)
tree = BeautifulSoup(page.text)
tree.find_all('tbody')

for tbody in tree.find_all('tbody'):
    for tr in tbody.find_all('tr'):
        for td in tr.find_all('td'):
            if u'Сальдо' in td:
                result = tr.text.split()[1]
print result