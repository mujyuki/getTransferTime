import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy
import csv
import re

def getTimeTrans(from_, to_):
	try:
		# Webページを取得して解析する
		# 6月14日9時40分到着
		load_url = "https://transit.yahoo.co.jp/search/result?flatlon=&fromgid=&from=" + from_ + "&tlatlon=&togid=&to=" + to_ + "&viacode=&via=&viacode=&via=&viacode=&via=&y=2021&m=06&d=14&hh=09&m2=0&m1=4&type=4&ticket=ic&expkind=1&ws=3&s=0&al=1&shin=1&ex=1&hb=1&lb=1&sr=1&kw="
		html = requests.get(load_url)
		soup = BeautifulSoup(html.content, "html.parser")

		timeStr = soup.find('span', class_='small').string
		# 分intへ変換
		times = re.findall(r"\d+", timeStr) #数字のみ抽出
		if len(times) >= 2:
			time = int(times[0]) * 60 + int(times[1])
		else:
			time = int(times[0])

		# transfer = int(soup.find('li', class_='transfer').find('span', class_='mark').string[:-1])
		return time

	except Exception as e:
		# raise e
		return -1
	

if __name__ == '__main__':

	filename = 'all_pref.csv'

	with open(filename) as f:
		reader = csv.reader(f)
		dfs=pd.DataFrame(index=[])
		columns=['pref', 'station_name', 'timeOote', 'timeTama']
		for row in reader:
			from_ = row[3]
			pref = row[1]
			if from_ == 'station_name' or from_ == '大手町' or from_=='多摩センター':
				continue
			timeOote = getTimeTrans(from_, '大手町')
			timeTama = getTimeTrans(from_, '多摩センター')
			dList = [[pref, from_, timeOote, timeTama]]
			df = pd.DataFrame(data=dList, columns=columns)
			# print(df)
			dfs = pd.concat([dfs, df])
			# print(dfs)
			print(from_, timeOote, timeTama)

	dfs.to_csv('out_all.csv', encoding="utf-8", index=False)

