#

# s = '21:20'
# s = s.split('-')
# print(s)
# print(datetime.date(s))
# t = datetime.localtime()
# print(t)
#t1 = (20, 20, 21)
# t1 = list(map(int, t1.split(':')))
#t3 = datetime.datetime(t1)
#print(t1)
#t2 = '20:50'
# t11 = time.strptime(t1, '%H:%M')
# t22 = time.strptime(t2, '%H:%M')
# rez = time.thread_time
# print(t11)
# print(t22)
# print(t22-t11)
import datetime
import time
t1 = time.strptime('20:20', '%H:%M')
t2 = time.strptime('20:50', '%H:%M')
print(t1)
print(t2)
print(datetime.datetime.now())
t1 = datetime.datetime(1980, 1, 1, t1[3], t1[4], 0)
t2 = datetime.datetime(1980, 1, 1, t2[3], t2[4], 0)
delta = t2 - t1
print(delta.total_seconds())

# b = (2017, 3, 5)
# a = datetime.datetime(b)
# print(a) # datetime.datetime(2017, 3, 5, 0, 0)
