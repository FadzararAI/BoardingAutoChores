from datetime import datetime
def piket_minggu():
	dt = datetime.now()
	day = dt.weekday()
	hour,minute,sec = dt.hour,dt.minute,dt.second
	print(hour)
	print(minute)
	if day == 6 and hour == 15 and minute == 30 and sec == 1:
		return True
	else:
		return False
