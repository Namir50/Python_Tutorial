a = {"Namir":4,"Ginger":1,"Ibaad":3,"Armaan":2}

x = sorted(a.items(),key = lambda x : x[1])
print(x)

x = sorted(a.items(),key = lambda x : x[1],reverse= True)
print(x)

print(sorted(a.values()))