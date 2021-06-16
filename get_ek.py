import requests
from bs4 import BeautifulSoup
import csv
import re

pref_list = ['tokyo', 'kanagawa', 'chiba', 'saitama']

def getEnsenName(pref):
	load_url = "https://suumo.jp/chintai/" + pref + "/ensen/"
	html = requests.get(load_url)
	soup = BeautifulSoup(html.content, "html.parser")
	patern = r'/chintai/' + pref + '/en_.*' #正規表現作成
	ensen_list = soup.find_all('a', attrs={ 'href': re.compile(patern) })
	url_list = [ i['href'] for i in ensen_list ] #リスト内包表記
	return url_list

for pref in pref_list:
	url_list = getEnsenName(pref)
	for target_url in url_list:
		load_url = "https://suumo.jp/" + target_url
		html = requests.get(load_url)
		soup = BeautifulSoup(html.content, "html.parser")
		print(load_url)
		resultset = soup.find_all('input', attrs={ 'name': 'ek', 'class': 'js-checkSingle js-checkEkiError js-fr-checkSingle' })

		with open('ek_test_all.csv', 'a') as f:
			writer = csv.writer(f)
			for result in resultset:
				print(result)
				ek = result['value']
				station_name = result.next_element.find('span').string
				writer.writerow([station_name, ek])


