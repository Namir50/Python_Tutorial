#first approach
l = [12,10,43,20,56]

for index, value in enumerate(l):
    print(index, value)

print()

#if we want start index to be 1
for index, value in enumerate(l,start = 1):
    print(index, value)

print()


#secoond approach
for i in range(0,len(l)):
    print(i,l[i])
