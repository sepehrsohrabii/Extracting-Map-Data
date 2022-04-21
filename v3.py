import pandas as pd
import json
from geopy.geocoders import Nominatim


geolocator = Nominatim(user_agent="geoapiExercises")

with open('los angles locations_Main.json', 'r') as json_file:
	json_load = json.load(json_file)

result = []
location = []
i = 1

for i in range(1, 6751):
	print(i)
	if json_load[i-1]["lat"] is None or json_load[i-1]["long"] is None:
		#print("is null")
		result.append(location)
		df1 = pd.DataFrame(result)
		df1.to_excel('output.xlsx', engine='xlsxwriter')
#		print(result)
		continue
	lat = json_load[i-1]["lat"]
	long = json_load[i-1]["long"]
	location2 = geolocator.reverse(lat + ", " + long)
	address = location2.raw['address']
	city = address.get('city', '')
	town = address.get('town', '')
	county = address.get('county', '')
	suburb = address.get('suburb', '')
	village = address.get('village', '')
	hamlet = address.get('hamlet', '')
	location = [lat, long, city, town, county, suburb, village, hamlet, address]
#	print(address)
	result.append(location)
	i = i + 1
#	print(result)

df1 = pd.DataFrame(result)
df1.to_excel('losangles_output_final_city.xlsx', engine='xlsxwriter')