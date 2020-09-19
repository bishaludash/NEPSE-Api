import schedule
import time
from shares import NepseScrapper

obj = NepseScrapper()
schedule.every(6).hours.do(obj.fetch_all_datas)
while 1 :
    schedule.run_pending()
    time.sleep(1)
