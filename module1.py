import requests
from bs4 import BeautifulSoup as BS

r = requests.get('https://www.udemy.com/course/learn_flutter')
html = BS(r.content, 'html.parser')
for el in html.select('.section--first-panel--2fbBU'):
    title = el.select('.udlite-btn')
    print(title[0].text)

for m in html.select('.section--first-panel--2fbBU'):
    text = m.select('li')
    for i in text:
        print(i.text)

###############Вывод в словарь
##items = html.find_all('div', class_='section--panel--1tqxC section--first-panel--2fbBU panel--panel--3NYBX')
##lessons = []
##for item in items:
##    lessons.append({
##        'text': item.find('ul', class_='unstyled-list udlite-block-list').get_text()
##    })
##print(lessons)



