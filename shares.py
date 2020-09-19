import urllib.request
import pandas as pd
import json

class NepseScrapper:
    """ Class to scrate data from NEPSE
        - Todays Share price
        - Top Gainers, Top Loosers
        - TODO : Top 10 Stocks by no. of transaction, Shares Traded,  Turnover
    """
    nepse_url = "http://www.nepalstock.com"
    todays_price = "http://www.nepalstock.com/todaysprice/export"

    def fetch_all_datas(self):
        """ 
        Entry function to fetch all NEPSE's data.
        """
        self.fetch_todays_share()
        self.fetch_gainers_and_losers()


    def fetch_todays_share(self):
        """ 
        Download the todays share data, process it and 
        save it into html and json file. 
        """
        try:
            print("Inside Fetch todays share function.")
            urllib.request.urlretrieve(self.todays_price, "templates/todays_share.html")
            
            df_list = pd.read_html('templates/todays_share.html')
            df = df_list[0].dropna(axis=0, thresh=4)
            todays_share_json = df.to_json(orient="records")

            with open('dumps/todayshare.json', 'w') as f:
                json.dump(json.loads(todays_share_json), f)

            print("Fetched todays share successfully.")
        except Exception as e:
            print('Could not dump todaysprice json. Exception : {}'.format(e))

    def fetch_gainers_and_losers(self):
        """
        Download the gainers and loosers data, process it and 
        save it into html and json file.
        """
        try:
            print("Inside fetch gainers and loosers function.")
            status = ["gainers", 'losers']
            for item in status:
                print("Processing for {}".format(item))
                url = "{}/{}".format(self.nepse_url, item)
                df = pd.read_html(url)
                df = df[0].dropna(axis = 0, thresh=3)
                df.columns = df.iloc[0]
                df = df.drop([0,1])
                df.to_html('templates/{}.html'.format(item), index = False)

                df_json = df.to_json(orient="records")
                with open('dumps/{}.json'.format(item), 'w') as f:
                    json.dump(json.loads(df_json), f)

                print("Processing complete for {}".format(item))
        except Exception as e:
            raise e

if __name__ == "__main__":
    obj = NepseScrapper()
    obj.fetch_all_datas()
