Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print ('\nExcercise Module 1 Excercise 3') 
import re
import datetime 
leave= "6:52:00"
easy= "0:08:15"
tempo= "0:07:12"
h,m,s = re.split(':',leave)
print int(datetime.timedelta(hours=int(h),minutes=int(m),seconds=int(s)).total_seconds())
h,m,s = re.split(':',easy)
print int(datetime.timedelta(hours=int(h),minutes=int(m),seconds=int(s)).total_seconds())
h,m,s = re.split(':',tempo)
print int(datetime.timedelta(hours=int(h),minutes=int(m),seconds=int(s)).total_seconds())
l1= 24720
e1= 495
t1= 432
seconds= (l1+e1+t1+.0)
minutes= (seconds/60)*(1.0)
hours= (minutes/60)*(1.0)
print "I will get home for breakfast at: ", hours 

print ('\nExcercise Module 1 Excercise 3 Variation 2')
import datetime

start = datetime.datetime(2016, 9, 8, 6, 52, 00) 
easyPace = datetime.timedelta(seconds=15, minutes=8)
tempo = datetime.timedelta(seconds=12, minutes=7)

time = start + easyPace + (tempo * 3) + easyPace
time = time.strftime(" %I:%M:%S")

print "I will get home for breakfast at: ", time

print ('\nExcercise Module 1 Excercise 3 Variation 3')

Excercise Module 1 Excercise 3
>>> 