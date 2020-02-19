from datetime import datetime, timedelta

# date = datetime.utcnow()

# # print(date.strftime("%a %d, %B %Y %H:%M %p"))

# result = "22 AM -1994 /October 10:22"

# dt_object = datetime.strptime(result, '%d %p -%Y /%B %H:%M')

# # print(date.strftime('%d %p -%Y /%m %H:%M'))
# print(dt_object)

############################################

date2 = "13-May-19"
day2 = "Mon"
time2 = "12:10 PM"

dt_object0 = day2 + ', ' + date2 + ' ' + time2
dt_object2 = datetime.strptime(dt_object0, '%a, %d-%B-%y %H:%M %p')

# dt_object0 = f'{day2}, {date2} {time2}'
# dt_object2 = datetime.strptime(dt_object0, '%a, %d-%B-%y %H:%M %p')

# dt_object0 = day2 + date2 + time2
# dt_object2 = datetime.strptime(dt_object0, '%a%d-%B-%y%H:%M %p')

# print(dt_object2)

#####################################################\

# another_date = dt_object2 + timedelta(days=1, hours=3)
# print(another_date)

now = datetime.utcnow()

registered_date = now - timedelta(days = 5)
registered_date = now - timedelta(days = 3)  #each variable overwrites above variables with the same name
registered_date = datetime(2020,2,10,2,57,34,465) #datetime is (year,month,day,hour,minute,second,mirosecond)
# registration expires 4 days after creation
check_date = now

print( check_date  <= registered_date + timedelta(days = 4))