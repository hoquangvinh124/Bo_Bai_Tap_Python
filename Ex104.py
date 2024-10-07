#Bai tap 104


x=int(input("Nhap x: "))
N=int(input("Nhap N: "))


def Tong(x,N):
   Tong = 0
   for i in range(1,N+1):
       Tu_so = x ** i
       Giai_thua = 1
       for j in range(1,i+1):
           Giai_thua = Giai_thua * j
       Tong += (Tu_so/Giai_thua)
   return Tong


print(f's({x},{N}) =',Tong(x,N))


