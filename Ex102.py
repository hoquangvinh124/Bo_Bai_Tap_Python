n=int(input('Nhap chieu cao: '))

def tamgiac(n):
    for i in range(1,n+1):
        for j in range(n-i):
            print(" ", end=" ")
        for z in range(i):
            print("*",end =" ")
        print('')

def hinhcn(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==1 or j==1 or i==n or j==n:
                print('* ',end='')
            else:
                print('',end='  ')
        print('')

def haitamgiac(n):
    for i in range(1,n+1):
        for j in range(1, n + 1):
            if i == j or i == (n + 1) / 2 or (i < (n + 1) / 2 and j == 1) or (i > (n + 1) / 2 and j == n):
                print('* ', end='')
            else:
                print('', end='  ')
        print('')


tamgiac(n)
hinhcn(n)
haitamgiac(n)