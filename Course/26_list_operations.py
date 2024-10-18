#count: returns count of an object
#index: return the index of an object
#pop: removes and returns the last element of a list
#remove: removes specific object from the list
#sort: sorts the data in the list
#insert: adds an element in dsired index
#append: adds element towards the end of the list
#extend

name = ["Namir", "Vahid", "Samira", "Ibaad", "Armaan"]
budget = [100,400,200,700,100]
print(budget.count(100))
print(budget.count(700))
print(budget.count(900))

print(budget.index(200))
print(budget.index(400))
print(name.index("Ibaad"))
print(name.index("Armaan"))

print(name.pop())
print(budget.pop())

print(name.remove("Namir"))
print(name)
print(budget.remove(200))
print(budget)

print(name.sort())
print(name)
print(budget.sort())
print(budget)

print(name.insert(3,"Namir"))
print(name.insert(4,"Armaan"))
print(budget.insert(3,200))
print(budget.insert(4,100))
print(name)
print(budget) 

print(name.append("Shah"))
print(budget.append(300))
print(name)
print(budget)
a = (name.append(budget))
print(a)

b = name.extend(budget)
print(b)


