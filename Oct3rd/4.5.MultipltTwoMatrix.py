A = [[6, 5, 3], [3, 2, 1], [1, 5, 4]]
B = [[5, 4, 6], [6, 9, 3], [4, 2, 2]]
C = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            C[i][j] += A[i][k] * B[k][j]
for resultMatrix in C:
    print(resultMatrix)
