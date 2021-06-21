![](https://i.imgur.com/WzqBk1p.png)

# NOTE
I have removed flask and schedurer as project dependency to reduce code footprint. The apis are served through github pages and the scrapping script run on cronjob.

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
Run the scrapper at 4pm daily.
```
0 16 * * * /usr/bin/python3 /path/to/NEPSE-Api/shares.py
```
