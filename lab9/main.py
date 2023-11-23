from datetime import datetime, date, timedelta


now = datetime.now()
print(now)
print(now.year)
month = now.strftime("%B")
print(month)

print(now + timedelta(days=5))

print(now - timedelta(weeks=2))

birth_date = "1990-05-28"
birth_date = datetime.strptime(birth_date, "%Y-%m-%d")

how_old = now - birth_date
print(how_old)