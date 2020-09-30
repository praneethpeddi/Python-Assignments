A = [[12, 7, 3], [4, 5, 6]]
B = [[5, 8, 1], [6, 7, 3]]
C = [[0, 0, 0], [0, 0, 0]]
for i in range(len(A)):
    for j in range(len(A[0])):
        C[i][j] = A[i][j] + B[i][j]
for resultMatrix in C:
    print(resultMatrix)
