
# 1
from datetime import datetime, timedelta

cur_time = datetime.now()
five_days_ago = cur_time - timedelta(days=5)
print(five_days_ago)

# 2

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print(f"Yesterday: {yesterday.strftime("%d/%m/%y")}, Today: {today.strftime("%d/%m/%y")}, Tomorrow: {tomorrow.strftime("%d/%m/%y")}")

# 3
cur_timee = datetime.now()
print (cur_timee.strftime("%H:%M:%S"))

# 4
day1 = datetime.now()
day2 = datetime(2007, 11, 13, 3, 13, 23)

diff = (day1 - day2).total_seconds()
print (diff)