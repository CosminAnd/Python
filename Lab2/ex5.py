import numpy as np

def modify_matrix(matrix):
    for i in range(len(matrix)):
        for j in range (len(matrix[0])):
            if(i>j):
                matrix[i][j]=0
    return matrix

matrix = np.array( [
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 5, 6],
        [1, 2, 3, 4, 5, 6]
        ] )

print(modify_matrix(matrix))
