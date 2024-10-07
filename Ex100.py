#Bai tap 100
import math


n = int(input('Vui long nhap n: '))
def dequycan2(n):
   if n == 0:
       return math.sqrt(2)
   else:
       return math.sqrt(2+dequycan2(n-1))


print(dequycan2(n))

