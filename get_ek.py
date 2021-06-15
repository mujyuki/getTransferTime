import requests
from bs4 import BeautifulSoup
import csv

pref_list = ['tokyo', 'kanagawa', 'chiba', 'saitama']
line_list = ['en_keiosen', 'en_odakyusen']

for pref in pref_list:
	for line in line_list:
		load_url = "https://suumo.jp/chintai/" + pref + "/" + line + "/"
		html = requests.get(load_url)
		soup = BeautifulSoup(html.content, "html.parser")

		resultset = soup.find_all('input', attrs={ 'name': 'ek' })

		# rn必要なし
		# rn = soup.find('input', attrs={ 'name': 'rn' })
		# print(rn['value'])

		with open('ek_test.csv', 'a') as f:
			writer = csv.writer(f)
			for result in resultset:
				ek = result['value']
				station_name = result.next_element.find('span').string
				writer.writerow([station_name, ek])


