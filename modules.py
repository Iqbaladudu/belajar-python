from datetime import datetime, date, time

# dt = datetime(2021, 9, 3)

# print(dt)

# get current day
# now_date = datetime(1, 1, 1)
ultah = datetime(2002, 3, 23)
print(ultah.strftime('%m=%d=%Y'))
now = datetime.now()
# print(now)
now_str = now.strftime('%H:%M')
print(now_str)

