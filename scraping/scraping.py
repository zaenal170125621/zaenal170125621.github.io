import requests
from bs4 import BeautifulSoup
import json
import time
from datetime import datetime

def dptInt(a):
    k = ''
    for i in range(2):
        if a[i] != ' ':
            k += a[i]
    return int(k)

def jamMenit(a):
    if 'menit' in a:
        return True
    else:
        return False

def get_current_time():
    current_time = datetime.now()
    return current_time.strftime('%Y-%m-%d %H:%M')

def fungsi(waktu):
    jamAtauMenit = jamMenit(waktu)
    n = dptInt(waktu)
    timestamp = time.time()
    if jamAtauMenit:
        timestamp -= n * 60
    else:
        timestamp -= n * 3600

    # Convert Unix timestamp to datetime object
    date_time = datetime.utcfromtimestamp(timestamp)

    # Format the datetime object as a string
    formatted_date = date_time.strftime('%Y-%m-%d %H:%M')
    return formatted_date

html = requests.get("https://www.republika.co.id/")
soup = BeautifulSoup(html.content, 'html.parser')
divs = soup.find_all('div', class_='caption')
dataset = []

for div in divs:
    subdiv = div.find('div')
    total = []
    try:
        kategoriNwaktu = subdiv.text.strip().split('- ')
        if len(kategoriNwaktu) == 2:
            kategori = kategoriNwaktu[0]
            waktu = kategoriNwaktu[1]
            total.extend((kategori, waktu))
    except AttributeError:
        pass

    subdiv = div.find('h3')
    if subdiv:
        title = subdiv.text.strip()
        total.append(title)

    if len(total) == 3:
        total[1] = fungsi(total[1])

        dataset.append({'kategori': total[0], 'judul': total[2], 'waktu_publish': total[1], 'waktu_scraping': get_current_time()})
        print(total[0])
        print(total[2])
        print(total[1])
        print(get_current_time())
        print()
print(len(dataset))

# Save dataset to JSON file
with open('data.json', 'w') as json_file:
    json.dump(dataset, json_file, indent=2)