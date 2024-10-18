import calendar

y = int(input("Enter year:"))
m = int(input("Enter month: "))

cal = calendar.month(y,m)
print(cal)