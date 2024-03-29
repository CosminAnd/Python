import numpy as np

def spiral_matrix(matrix):
    col = len(matrix)
    row = len(matrix[0])

    top = 0
    bottom = row - 1
    left = 0
    right = col - 1

    direction = 0

    while top <= bottom and left <= right:
        if direction == 0: #right
            for i in range(left, right+1):
                print(matrix[top][i], end=" ")
            top += 1
            direction = 1
        elif direction == 1: #bottom
            for i in range(top, bottom+1):
                print(matrix[i][right], end=" ")
            right -= 1
            direction = 2
        elif direction == 2: #left
            for i in range(right, left-1, -1):
                print(matrix[bottom][i], end=" ")
            bottom -= 1
            direction = 3
        elif direction == 3: #top
            for i in range(bottom, top-1, -1):
                print(matrix[i][left], end=" ")
            left += 1
            direction = 0


matrixx = np.array(
    [
        ["f", "i", "r", "s"],
        ["n", "_", "l", "t"],
        ["o", "b", "a", "_"],
        ["h", "t", "y", "p"]
    ]
)

spiral_matrix(matrixx)
