#Sum of Diagonals of list
from typing import List

mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]
n = len(mat)
right = sum(mat[i][i] for i in range(n))
print(right)

left = sum(mat[i][n-i-1] for i in range(n))
print(left)



