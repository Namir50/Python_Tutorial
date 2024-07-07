#count
#index
#length
#concatenation
#tuple top list , list to tuple


t = (1,4,6,77,5,2,10,1,6)
z = (5,2,4,6,10,4,90,32)
x = [1,3,4,5,5,6,3,6]
 
print(t.count(6))
print(t.count(4))
print(t.count(1))

print(t.index(77))
print(t.index(1))
print(t.index(2))   

print(len(t))

print(t + z)
print(t*2)
print(z*2)

tl = list(t)
print(type(tl))
zl = list(z)
print(type(z))

xt = tuple(x)
print(type(xt))

