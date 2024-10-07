#Bai tap 107

x = int(input('Vui long nhap x: '))
n = int(input('Vui long nhap n: '))

s = 0
for i in range(1,2*n+2,2):
   tu_so = x**i
   giai_thua = 1
   for j in range(1,i+1):
       giai_thua = giai_thua * j
   s += tu_so/giai_thua
print (f's({x},{n})=',s)




