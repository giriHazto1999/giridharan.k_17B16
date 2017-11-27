def matrixmulti(x, y):
    m = len(x)
    n = len(x[0])
    p = len(y[0])
    z = [[0] * p for row in range(m)]
    if n != len(y):
        print("Incorrect dimentions.")
        return
    for i in range(m):
        for j in range(p):
            for k in range(n):
                z[i][j] += x[i][k]*y[k][j]


    return z
x = [[1,2],[1,1]]
y = [[1, 2, 1], [1, 2, 1]]
print matrixmulti(x,y)
