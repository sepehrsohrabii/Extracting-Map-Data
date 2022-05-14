import requests
import pandas as pd
import json
import time

#sample link = "https://data.lamar.com/inventorybrowsing/Inventory/index?callback=jQuery110207797654875936315_1651308122786&inventories={%22current%22:{%22points%22:[{%22lat%22:40.71427,%22long%22:-74.00597},{%22lat%22:34.05223,%22long%22:-118.24368},{%22lat%22:41.85003,%22long%22:-87.65005},{%22lat%22:29.76328,%22long%22:-95.36327},{%22lat%22:39.95233,%22long%22:-75.16379},{%22lat%22:33.44838,%22long%22:-112.07404},{%22lat%22:29.42412,%22long%22:-98.49363},{%22lat%22:32.71571,%22long%22:-117.16472},{%22lat%22:32.78306,%22long%22:-96.80667},{%22lat%22:40.6501,%22long%22:-73.94958},{%22lat%22:40.68149,%22long%22:-73.83652},{%22lat%22:37.33939,%22long%22:-121.89496},{%22lat%22:30.26715,%22long%22:-97.74306},{%22lat%22:30.33218,%22long%22:-81.65565},{%22lat%22:37.77493,%22long%22:-122.41942},{%22lat%22:39.96118,%22long%22:-82.99879},{%22lat%22:32.72541,%22long%22:-97.32085},{%22lat%22:39.76838,%22long%22:-86.15804},{%22lat%22:35.22709,%22long%22:-80.84313},{%22lat%22:40.78343,%22long%22:-73.96625}]},%22exclusionShapes%22:[]}&_=1651308122794"
lat = ""
long = ""
lat_long = ''
lat_longs = ''
i = 1
result = ''

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
    'Connection': 'keep-alive',
    'Referer': 'http://apps.lamar.com/',
    'Sec-Fetch-Dest': 'script',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
}


with open('csvjson.json', 'r') as json_file:
	json_load = json.load(json_file)

for i in range(1, 28339):
	print(i)
	lat = json_load[i-1]["lat"]

	long = json_load[i-1]["lng"]

	lat_long = '{{%22lat%22:{} ,%22long%22:{}}}'.format(lat, long)

	if lat_longs == '':
		lat_longs = lat_long
	else:
		lat_longs = lat_longs +', '+ lat_long

	if i % 20 == 0:
		link = "http://data.lamar.com/inventorybrowsing/Inventory/index?inventories={%22current%22:{%22points%22:[" + lat_longs + "]}}"
		try:
			response = requests.get(link, headers=headers)
		except:
			time.sleep(900)
			response = requests.get(link, headers=headers)
		result = response.text
		lat_longs = ''
		with open("response2.txt", "a") as r:
			r.write(result)

	if 28320 > i >= 28339:
		link = "http://data.lamar.com/inventorybrowsing/Inventory/index?inventories={%22current%22:{%22points%22:[" + lat_longs + "]}}"
		try:
			response = requests.get(link, headers=headers)
		except:
			time.sleep(900)
			response = requests.get(link, headers=headers)
		result = response.text
		with open("response2.txt", "a") as r:
			r.write(result)

	i = i + 1



#with open('response.txt', 'w') as r:
#	r.write(result)

#df1 = pd.DataFrame(response.text)
#df1.to_excel('usa.xlsx', engine='xlsxwriter')
