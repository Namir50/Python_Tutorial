#count the number of unique words in a sentence
sent = "Be the change you wish to see in the world"
lst = sent.split()
print(lst)

a = (set(lst))
print(a)
print(len(a))