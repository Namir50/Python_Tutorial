l = []
for i in range(10):
    l.append(i**2)
print(l)


a = [i for i in range(20)]
print(a)

b = [i for i in range(0,20,2)]
print(b)

c = [i**2 for i in range(20)]
print(c)


x = 10
for i in range(x):
    if i%2==0:
        print(i)

for i in range(x):
    if i%2==1:
        print(i)