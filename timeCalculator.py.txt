import datetime
import dateutil.relativedelta

# current time
date_and_time = datetime.datetime.now()
date_only = date.today()
time_only = datetime.datetime.now().time()

# calculate date and time
result = date_and_time - datetime.timedelta(hours=26, minutes=25, seconds=10)

# calculate dates: years (-/+)
result = date_only - dateutil.relativedelta.relativedelta(years=10)

# months
result = date_only - dateutil.relativedelta.relativedelta(months=10)

# days
result = date_only - dateutil.relativedelta.relativedelta(days=10)

# calculate time 
result = date_and_time - datetime.timedelta(hours=26, minutes=25, seconds=10)
result.time()