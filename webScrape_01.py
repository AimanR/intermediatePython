#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import pandas as pd


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

'''
print(items[0])


print(items[0].find(class_='period-name').get_text())
print(items[0].find(class_='short-desc').get_text())
print(items[0].find(class_='temp').get_text())
'''


period_names = [item.find(class_='period-name').get_text() for item in items] ;# print(period_names)
short_descriptions = [item.find(class_='short-desc').get_text() for item in items] ;# print(short_descriptions)
temperature = [item.find(class_='temp').get_text() for item in items] ;# print(temperature)


weather_stuff = pd.DataFrame(
    {
        'Period':period_names,
        'Short description':short_descriptions,
        'Temperature':temperature,
    })

print(weather_stuff)

weather_stuff.to_csv('Weather.csv')