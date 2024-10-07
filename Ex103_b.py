def pascal(m):
    n = 2*m+1
    mid = n // 2
    A = [[0 for _ in range(m)] for _ in range(n)]

    A[mid][0] = 1

    for j in range(1, m): #cot :m
        for i in range(n): #dong:n
            if i < n - 1:
                A[i][j] += A[i - 1][j - 1]
                A[i][j] += A[i + 1][j - 1]

    for i in range(n):
        for j in range(m):
            if A[i][j] != 0:
                print(f"{A[i][j]} ", end="")
            else:
                print("  ", end="")
        print()

m = int(input('Nhap chieu cao: '))
pascal(m)
