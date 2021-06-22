import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

ploads={'_limit':500}
url = "http://www.nepalstock.com/company"
cwd = os.path.dirname(os.path.abspath(__file__))

def listedCompanyScrapper():
   try:
      print("Inside Fetch listed company function.")
      r = requests.post('http://www.nepalstock.com/company', params=ploads)
      if r.status_code is not 200:
         exit()

      html_file = r.text
      soup = BeautifulSoup(html_file, 'lxml')
      match = soup.table
      match.find('form', id="company-filter").decompose()

      # replace anchor tag with link only
      for div in match.findAll('a', class_="icon-view"):
         div.replace_with(div['href'])

      df = pd.read_html(str(match))
      # drop first empty rows
      df = df[0].drop([0])
      # drop NAN columns
      df = df.drop(columns=[1,6,7,8,9,10,11])

      # set first row as columns and drop it
      # Also drop last column as it pagination number
      df.columns = df.iloc[0]
      total_rows = df.shape[0]
      df = df.drop([1, total_rows])

      print("Dumping listed company table.")
      df.to_html('{}/templates/listedCompany.html'.format(cwd), index = False)

      print("Dumping listed company api.")
      df_json = df.to_json(orient="records")
      with open('{}/dumps/listedCompany.json'.format(cwd), 'w') as f:
         json.dump(json.loads(df_json), f, indent=4, sort_keys=True)
   except Exception as e:
      print('Could not dump listed companies. Exception : {}'.format(e))
   
listedCompanyScrapper()