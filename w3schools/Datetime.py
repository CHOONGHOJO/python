import datetime
 
print (datetime.datetime.now())  # 2020-03-15 08:03:34.910860
print (datetime.datetime.today()) # 2020-03-15 08:03:34.910860    
print (datetime.date.today()) # 2020-03-15

from datetime import date
print (date.today()) # 2020-03-15
today = date.today()
print(today.year)
print(today.month)
print(today.day)

from datetime import datetime

# current date and time
now = datetime.now()

t = now.strftime("%H:%M:%S")
print("time:", t)
print(now.strftime("%H:%M:%S"))

s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)





