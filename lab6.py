from datetime import datetime, date, timedelta
import calendar

date = datetime.now()
print(date)
print(date.year)
print(date.strftime("%Y"))

print(date.strftime("%B"))

print(date.strftime("%A"))

date_object = datetime.strptime("2023-11-15", "%Y-%m-%d")
print(date_object)

date_object = datetime.strptime("2023-Nov-15", "%Y-%b-%d")
print(date_object)

date_object = datetime.strptime("2023-Nov-15", "%Y-%b-%d")
new_date = date_object + timedelta(days=5)
print(new_date)


print(date-timedelta(weeks=2))


new_year = datetime.strptime("2023-Jan-1", "%Y-%b-%d")
print((date - new_year).days)

new_year = calendar.isleap(2024)
print(new_year)

rfc_date = datetime.strptime('2023-11-15 00:00:00', "%Y-%m-%d %H:%M:%S").strftime("%a, %d %b %Y %H:%M:%S +0000")
print(rfc_date)

past_date = datetime(date.year, 7, 4)
print(past_date.strftime("%A"))