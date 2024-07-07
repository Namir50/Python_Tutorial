a = [[1,4,6],
     [10,2,7],
     [6,7,9]]

b = [[3,1,8],
     [6,7,4],
     [7,8,10]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for i in range(len(a)):
    for j in range(len(a[0])):
        result[i][j] = a[i][j] * b[j][i]
print(result)

