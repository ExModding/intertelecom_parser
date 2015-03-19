#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


URL = 'https://assa.intertelecom.ua/ru/login'
LOGIN = '442216339'
PASSWORD = 'LookS2014s'

requests.packages.urllib3.disable_warnings()
payload = {'phone': LOGIN, 'pass': PASSWORD}
page = requests.post(URL, data=payload, )

tree = BeautifulSoup(page.text)
tree.find_all('tbody')

for tbody in tree.find_all('tbody'):
    for tr in tbody.find_all('tr'):
        for td in tr.find_all('td'):
            if u'Сальдо' in td:
                print tr.text.split()[1]
                break