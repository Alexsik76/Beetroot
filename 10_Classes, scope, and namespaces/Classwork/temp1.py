from datetime import datetime
t4 = datetime.strptime('20:20', '%H:%M')
t5 = datetime.strptime('20:50', '%H:%M')
print(t4)
print(t5)
t1 = t5 - t4
x = t1 * 200
print(x)
