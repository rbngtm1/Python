# Rotate image problem from Leetcode
import numpy as np
input_matrix= [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]]

print(type(input_matrix))


input_matrix = np.array(input_matrix)
print(type(input_matrix))
transpose_matrix = input_matrix.transpose()

temp = []
# print(res)
for i in range (0,len(input_matrix)):
    A = list(transpose_matrix[i])
    A.reverse()
    temp.append(A)
print(temp)
 