a = [[1,4,5],
     [3,5,6],
     [3,10,7]]

b = [[2,10,12],
     [3,5,6],
     [10,15,2]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(len(a)):
    for j in range(len(a[0])):
        result[i][j]  = a[i][j] + b[i][j]

print(result)