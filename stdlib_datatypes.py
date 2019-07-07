#data types
#built in: dict, list, set, frozenset, tuple, str class is used to hold unicode strings, bytes class to hold binary data

from datetime import date, datetime, time, timezone, timedelta


print("--------------------------------")
print("date time stuff")
mydate = date(2019, 12, 8)
tuday = date.today()
print(tuday)
mytime = time()
#print("time is:", mytime.time())
mydatetime = datetime(2019, 12, 8)
#mytimezone = datetime.timezone()
print("date objects are naive, time or datetime may or may not be, depends if timezone is associated")
mytimedelta = timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)


