#like lists tuples are ordered collection of data
#unchangeable (ummutable)
#iterable
#heterogenous


#non empty tuple with single data
a = (2,)
print(type(a))
b = ("Namir",)
print(type(b))


p = ("Namir", "Vahid", "Samira", "Armaan", "Ibaad")
#indexing
print(p)
print(p[1])
print(p[2])
print(p[0:])
print(p[::])
print(p[1:3])
print(p[:4])

#unchangeable
#p[0] = "Hello"     - this is an error

#iterable
for i in p:
    print(i)

#heterogenous
z = (45, "Hello", 78.5, "Nice", 0)
print(type(z))
print(z)
print(z[0])
print(z[1:3])

for i in z:
    print(i)


#list inside tuple
c = ([1,2,3], [4,5,6], [7,8,9])
print(type(c))
print(c)