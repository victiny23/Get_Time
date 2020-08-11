import time
from datetime import datetime
"""
%a 	Locale’s abbreviated weekday name. 	 
%A 	Locale’s full weekday name. 	 
%b 	Locale’s abbreviated month name. 	 
%B 	Locale’s full month name. 	 
%c 	Locale’s appropriate date and time representation. 	 
%d 	Day of the month as a decimal number [01,31]. 	 
%H 	Hour (24-hour clock) as a decimal number [00,23]. 	 
%I 	Hour (12-hour clock) as a decimal number [01,12]. 	 
%j 	Day of the year as a decimal number [001,366]. 	 
%m 	Month as a decimal number [01,12]. 	 
%M 	Minute as a decimal number [00,59]. 	 
%p 	Locale’s equivalent of either AM or PM. 	(1)
%S 	Second as a decimal number [00,61]. 	(2)
%U 	Week number of the year (Sunday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Sunday are considered to be in week 0. 	(3)
%w 	Weekday as a decimal number [0(Sunday),6]. 	 
%W 	Week number of the year (Monday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Monday are considered to be in week 0. 	(3)
%x 	Locale’s appropriate date representation. 	 
%X 	Locale’s appropriate time representation. 	 
%y 	Year without century as a decimal number [00,99]. 	 
%Y 	Year with century as a decimal number. 	 
%Z 	Time zone name (no characters if no time zone exists). 	 
%% 	A literal '%' character.
"""

"""Get time from system"""
## 24 hour format ##
print (time.strftime("%H:%M:%S"))

## 12 hour format ##
print (time.strftime("%I:%M:%S"))

## dd/mm/yyyy format
print (time.strftime("%d/%m/%Y"))

## mm/dd/yy format
print (time.strftime("%m/%d/%y"))

## dd/mm/yyyy hh:mm:ss format
print (time.strftime('%d/%m/%Y %H:%M:%S'))

## mm/dd/yyyy hh:mm:ss format
print (time.strftime('%m/%d/%Y %H:%M:%S'))

time1 = time.gmtime()
time2 = time.localtime()
## yyyy-mm-dd weekday_full_name
print(time.strftime('%Y-%m-%d %A', time1))
## yyyy week_number week_day
print(time.strftime('%Y Week %W Day %w', time2))
## weekday_abbreviated_name, dd month_abbreviated_name yyyy hh:mm:ss
print(time.strftime('%a, %d %b %Y %H:%M:%S GMT', time2))



"""Get time object in Python from strings"""
time_str = 'Wed, 20 Feb 2013 23:52:14 GMT'
print(time.strptime(time_str, '%a, %d %b %Y %H:%M:%S GMT'))

iso8601 = '2013-02-20T23:52:14'
print(time.strptime(iso8601, '%Y-%m-%dT%H:%M:%S'))

time_dict = {'month': 4, 'day': 25, 'year': 1993, 'hour': 6, 'min': 15}
t_string = '{}/{}/{} {}:{}'.format(
    time_dict['month'], time_dict['day'], time_dict['year'], time_dict['hour'], time_dict['min'])
print(time.strptime(t_string, '%m/%d/%Y %H:%M'))

# time object from string
t_reform = time.strptime(t_string, '%m/%d/%Y %H:%M')
print(type(t_reform)) 
# string from time object
print(time.strftime('%Y/%m/%d %H:%M%p', t_reform))

"""Convert time struct object to datetime object"""
# time struct object (time turple) --(time.mktime)--> seconds since the Epoch
# --(datetime.fromtimestamp)--> datetime object
start_time = datetime.fromtimestamp(time.mktime(time.localtime()))
a = []
for i in range(1000**2):
    if i % 3 == 0:
       a.append(-i)
    elif i % 3 == 1:
        a.append(2*i)
    else:
         a.append(float(i/3))
b = a[-10:][::-1]

print(b[0])
end_time = datetime.fromtimestamp(time.mktime(time.localtime()))
duration = end_time - start_time
print(duration.total_seconds())












