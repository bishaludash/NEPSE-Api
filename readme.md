![](https://i.imgur.com/WzqBk1p.png)
#NOTE
I have remove flask and schedures as project dependency to reduce code footprint and now the scrapping script run on cronjob.

# Setup
Here are the list of python packages requires:
- Pandas => pip install pandas
- lxml => pip install lxml

## Scrape Todays share
Run the script shares.py to fetch the Todays share data.

```
python3 shares.py

```

## Add below code in crontab run in cronjob
```
/usr/bin/python3 /path/to/NEPSE-Api/shares.py
```
