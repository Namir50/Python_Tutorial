#DATA STRUCTURES IS A SPECIALIZED FORMAT FOR ORGANIZING, PROCESSING, RETRIEVING AND STORING DATA

#Lists are ordered collection of data
#Lists are mutable type of data
#It can contain multiple type of data
#Lists are changeable
#lists are iterable

l1 = [1,2,7,8,6]
print(type(l1))

print(len(l1))
print(l1[0])
print(l1[3])
print(id(l1))
print(id(l1[2]))


#Mutability(changing/updating)
l1[2]= 8
print(l1)

l1[4]= 9
print(l1)


#iterable
for i in l1:
    print(i)


class Solution:
    def str(self, haystack:str, needle:str) -> int:
        for i in haystack:
            print(i)
        for i in needle:
            print(i)

sol = Solution()
sol.str("sadness", "sad")