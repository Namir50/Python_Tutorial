#using union operator
a = {"Namir": 95,"Ibaad": 98,"Ironman":93}
b = {"Ibaad":99,"Superman":100}

print(a | b)

#using exponential operator
print({**a,**b})

#using copy and update(it will get us the first value of common key)
c = b.copy()
c.update(a)
print(c)