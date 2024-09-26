#find frequency of every each letter in a string    
name = (input("Your name:"))

freq = {}
for i in name:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i]+=1
print(freq)
