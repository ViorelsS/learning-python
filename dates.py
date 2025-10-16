import datetime

x = datetime.datetime.now()
x = x.strftime("%B")
y = datetime.datetime(2012, 7, 13)

print(x)
print(y)

print(y.strftime("%d/%m/%y"))
