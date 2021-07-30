import requests
from bs4 import BeautifulSoup
import csv
import re


ek = '02403013'
load_url = "https://suumo.jp/jj/chintai/ichiran/FR301FC001/?ar=030&bs=040&ra=013&ek=02403013&cb=0.0&ct=9999999&mb=0&mt=9999999&md=06&et=10&cn=9999999&shkr1=03&shkr2=03&shkr3=03&shkr4=03&sngz=&po1=25&pc=50"

ua = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
headers = {'user-agent':ua}


html = requests.get(load_url)
print(html.text)
soup = BeautifulSoup(html.content, "html.parser")
yatin_list = soup.find_all('li')
print(yatin_list)
for yatin in yatin_list:
	print(yatin.string)