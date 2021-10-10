import datetime
import pytz

# Naive and aware datetime- Naive doesn't have additional information like timezones, daylight saving etc

d = datetime.date(2021, 12, 28)
print(d)

# Today
today = datetime.date.today()
print(today)
print(today.year)
print(today.weekday())
print(today.isoweekday()) # weekday starts with 0 for Monday while isoweekday is +1

# Timedeltas
tdelta = datetime.timedelta(days=7)
print(today + tdelta)
print(today - tdelta)

# Adding/Subtracting dates returns a timedelta
days_till_bday = d - today
print(days_till_bday)
print(days_till_bday.total_seconds())

# datetime.time
t = datetime.time(9, 30, 45, 1000)
print(t.hour)
dt = datetime.datetime(2021, 5, 30, 20, 28, 45, 1000)
print(dt)
tdelta = datetime.timedelta(hours=12)
print(dt + tdelta)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today,'\n',dt_now,'\n',dt_utcnow)

# dt_today has no tz info, dt_now gives option to pass a timezone, utc_now gives utc time but still has no tz info
dt_timezone = datetime.datetime(2021, 5, 30, 20, 28, 45, 1000, tzinfo=pytz.utc)
print(dt_timezone)

dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)

# Convert to current timezone- List of timezones- https://www.youtube.com/watch?v=eirjjyP2qcQ
dt_current_tz = dt_utcnow.astimezone(pytz.timezone('Asia/Kolkata'))
print(dt_current_tz)

# Get all timezones
for tz in pytz.all_timezones:
    print(tz)

# Adding tz info to a naive datetime
dt_ist = datetime.datetime.now()