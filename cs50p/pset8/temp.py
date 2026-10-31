from datetime import date

date_today = date.today()
timedelta = date_today - date(2000, 1, 1)
print(timedelta)
print(timedelta.days)