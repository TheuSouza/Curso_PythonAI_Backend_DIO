from datetime import datetime
import pytz

d = datetime.now(pytz.timezone('Asia/Tokyo'))
u = datetime.now(pytz.timezone('UTC'))

print(d)
print(u)