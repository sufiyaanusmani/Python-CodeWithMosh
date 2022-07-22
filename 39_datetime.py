from datetime import datetime
import time

dt = datetime(2018, 1, 2)
print(dt)
print(datetime.now())
print(datetime.strptime("2018/01/01", "%Y/%m/%d"))
print(datetime.fromtimestamp(time.time()))

print(f"{dt.year}/{dt.month}")
print(dt.strftime("%Y/%m"))
