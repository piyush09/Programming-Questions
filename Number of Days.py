import datetime
from datetime import date
from datetime import timedelta

startDate = "2019-01-01 00:00"
endDate = "2019-01-05 01:00"
n = 1

firstdatepart = startDate.split()
# print (firstdatepart)
temp = firstdatepart[0]
date1 = firstdatepart[0].split('-')
date2 = firstdatepart[1].split(':')

d1 = datetime.datetime(int(date1[0]), int(date1[1]), int(date1[2]), int(date2[0]), int(date2[1]))
# print (d1)

initial_date = date(int(date1[0]), int(date1[1]), int(date1[2]))

seconddatepart = endDate.split()
# print (seconddatepart)

date3 = seconddatepart[0].split('-')
date4 = seconddatepart[1].split(':')

d2 = datetime.datetime(int(date3[0]), int(date3[1]), int(date3[2]), int(date4[0]), int(date4[1]))
# print (d2)

final_date = date(int(date3[0]), int(date3[1]), int(date3[2]))

number_days = (final_date - initial_date).days
print("Number of days are:")
print (number_days)


# def time_stamp(date1, number_days):
#     add_hour = timedelta(hours=1)
#     print ("In Function")
#     # pass_date = datetime(date1)
#     print (date1)
#     print (number_days)
#
#
#     timelist = []
#
#     for i in range(24*number_days):
#         timelist.append(date1.strftime("%Y-%m-%d %H:%M"))
#         date1 += add_hour
#
#     print (timelist)
#     print (len(timelist))

# time_stamp(d1, number_days)





