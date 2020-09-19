![](https://i.imgur.com/WzqBk1p.png)

# Setup

Here are the list of python packages requires:
- Pandas
- Flask
- Schedule
- lxml

## Scrape Todays share
Run the script download_scheduler.py to fetch the Todays share on background. Data is updated every 6 hour .

```
nohup python download_scheduler.py &

```

## Run the app to serve apis

Start the server in development mode by running command below
```
python app.py
``` 

### Running  app server background
```
nohup python app.py &
```
