from datetime import date
 
today = date.today()
print(today)      # 2017-05-03
print("{}.{}.{}".format(today.day, today.month, today.year))      # 2.5.2017


from datetime import time
 
current_time = time()
print(current_time)     # 00:00:00
 
current_time = time(16, 25)
print(current_time)     # 16:25:00
 
current_time = time(16, 25, 45)
print(current_time)     # 16:25:45


from datetime import datetime
 
now = datetime.now()
print(now)     # 2017-05-03 11:18:56.239443
 
print("{}.{}.{}  {}:{}".format(now.day, now.month, now.year, now.hour, now.minute))  # 3.5.2017  11:21
 
print(now.date())
print(now.time())


from datetime import datetime
deadline = datetime.strptime("22/05/2017", "%d/%m/%Y")
print(deadline)     # 2017-05-22 00:00:00
 
deadline = datetime.strptime("22/05/2017 12:30", "%d/%m/%Y %H:%M")
print(deadline)     # 2017-05-22 12:30:00
 
deadline = datetime.strptime("05-22-2017 12:30", "%m-%d-%Y %H:%M")
print(deadline)     # 2017-05-22 12:30:00
