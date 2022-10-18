"""def ex9 (matrix):
    rez=[]
    for i in range(1,len(matrix)):
        for j in range(len(matrix[i])):
            if(matrix[i][j] <= matrix[i-1][j]):
                rez.append((i, j))
    return rez


matrix = [
[1, 2, 3, 2, 1, 1],

[2, 4, 4, 3, 7, 2],

[5, 5, 2, 5, 6, 4],

[6, 6, 7, 6, 7, 5]
]

print(ex9(matrix))"""


def ex9(matrix):
    rez = []
    for index in range(len(matrix) - 1, -1, -1):
        for j in range(0, len(matrix[index]), 1):
            for i in range(index - 1, -1, -1):
                if matrix[index][j] <= matrix[i][j]:
                    rez.append((index, j))
                    break
    return rez


matrix = [[1, 2, 3, 2, 1, 1],
          [2, 4, 4, 3, 7, 2],
          [5, 5, 2, 5, 6, 4],
          [6, 6, 7, 6, 7, 5]]

print(ex9(matrix))
