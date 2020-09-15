# Setup

Here are the list of python packages requires:
- Pandas
- Flask
- Schedule

## Scrape Todays share
Run the script download_share.py to fetch the Todays share on background. Data is updated every 6 hour .

```
nohup python3 download_scheduler.py &

```

## Run the app to serve apis
If you have not scraped data before starting the server, run the command below
```
python3 download_share.py
```  

Start the server in development mode by running command below
```
python app.py
``` 

### Running in app server background
```
nohup python3 app.py &
```
