x = [[1,2,4],
    [4,5,6]]

transposed = [[0 for _ in range(len(x))] for _ in range(len(x[0]))]

for i in range(len(x)):
    for j in range(len(x[0])):
        transposed[j][i] = x[i][j]
print(transposed)


#Second method
T = [[x[j][i] for j in range(len(x))] for i in range(len(x[0]))]
print(T)


