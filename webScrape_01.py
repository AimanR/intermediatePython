#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

page = requests.get("https://forecast.weather.gov/MapClick.php?lat=34.05361000000005&lon=-118.24549999999999#.X93bm1MzaV4")
soup = BeautifulSoup(page.content, 'html.parser')

week = soup.find(id='seven-day-forecast-body')

'''
print(week)
'''

'''
x = week.find_all('li')
for li in x:
    print(li)
    print()
'''

items = week.find_all(class_='tombstone-container')
print(items[0])