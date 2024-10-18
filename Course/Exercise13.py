#add unique elements into a new list from exisiting list
list = [1,2,3,4,3,2,5,6,5,7]

def func(li):
    new = []
    for i in li:
        if i not in new:
            new.append(i)
    return new

print(func(list))


a = [[1,2,3],[4,5,6]]
for row in a:
    for elements in row:
        print(elements)