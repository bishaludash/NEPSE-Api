import urllib.request

import pandas as pd
import json

todays_price = "http://www.nepalstock.com/todaysprice/export"

try:
	urllib.request.urlretrieve(todays_price, "templates/todays_price.html")
	
	df_list = pd.read_html('templates/todays_price.html')
	df = df_list[0].dropna(axis=0, thresh=4)
	todaysprice_json = df.to_json(orient="records")


	with open('dumps/todaysprice.json', 'w') as f:
	    json.dump(json.loads(todaysprice_json), f)
except Exception as e:
	print('Could not dump todaysprice json. Exception : {}'.format(e))