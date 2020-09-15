import schedule
import time
import shares

schedule.every(6).hours.do(shares.fetch_todays_share)
while 1 :
	schedule.run_pending()
	time.sleep(1)