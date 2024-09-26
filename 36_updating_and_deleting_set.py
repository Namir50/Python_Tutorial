s = {1,3,4,5,6,7,4,2}
print(s)

# add single element to set using the `add()` method:
s.add(9)
print(s)

#update
a = set("namir shah")
s.update(a)
print(s)

for i in s:
    print(i)

b = {10,9,56,34}
s.update(b)
print(s)

for i in s:
    print(i)


#pop() removes random data from the set and returns it
#remove() removes desired element from the set
(s.pop())
print(s)

(s.remove(7))
print(s)

b = set("hello everyone")
print(type(b))

b.pop()
print(b)

b.remove("o")
print(b)
