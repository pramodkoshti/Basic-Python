# Python we need to import the datetime module

import datetime

today_date = datetime.datetime.now()
print(today_date)

# date objects creation

tomorrow_date = datetime.datetime(2018,12,17)
print(tomorrow_date)

# There are many functions in datetime moudle 

print(today_date.year)
print(today_date.day)
print(today_date.month)

# strftime functions used to format the date in readable formats

print(today_date.strftime("%A")) # name of weekday
print(today_date.strftime("%B")) # name of the Month 