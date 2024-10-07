#Bai tap 108


def perfect_number(n):
   s = 0
   for i in range(1,n):
       if n % i == 0:
           s += i
   if s == n:
       return print(f'{n} la so hoan hao')
   else:
       return print(f'{n} khong phai la so hoan hao')


def abundant_number(n):
   s = 0
   for i in range(1, n):
       if n % i == 0:
           s += i
   if s > n:
       return print(f'{n} la so phong phu')
   else:
       return print(f'{n} khong phai la so phong phu')

n = int(input('Vui long nhap so nguyen duong: '))
perfect_number(n)
abundant_number(n)




