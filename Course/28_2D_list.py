a = [1,2,3]
b = [4,5,6]
c = [7,8,9]

x = [a,b,c]

print(type(x))
print(x)

#indexing
print(x[0])
print(x[1])
print(x[2])

print(x[0][0])
print(x[0][1])
print(x[0][2])

print(x[1][0])
print(x[1][1])
print(x[1][2])

print(x[2][0])
print(x[2][1])
print(x[2][2])

#iteration
for i in x:
    print(i)


for i in x:
    for j in i:
        print(j)