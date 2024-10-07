def pascal(m):
    n = 2*m+1
    mid = n // 2
    A = [[0 for _ in range(m)] for _ in range(n)]

    A[mid][m-1] = 1

    for j in range(m, 0, -1): #cot :m
        for i in range(n-1): #dong:n
            if j < m:
                A[i][j-1] += (A[i - 1][j])
                A[i][j-1] += (A[i + 1][j])
            if A[i][j-1] > 1:
                A[i][j-1] +=1

    for i in range(n):
        for j in range(m):
            if A[i][j] != 0:
                print(f"{A[i][j]:2d}", end="")
            else:
                print("  ", end="")
        print()

m = int(input('Nhap chieu cao: '))
pascal(m)