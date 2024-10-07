#Bai tap 79
import math


a = float(input("Nhap canh tam giac a (a>0): "))
b = float(input("Nhap canh tam giac b (b>0): "))
c = float(input("Nhap canh tam giac c (c>0): "))


def Tinh_dien_tich_tam_giac(a,b,c):
   cv = a+b+c
   p = cv/2
   dt = math.sqrt(p*(p-a)*(p-b)*(p-c))
   return dt


if a<=0 or b<=0 or c<=0 or (a+b)<=c or (a+c)<=b or b+c<=a:
   print('Canh khong hop le vui long nhap lai')
else:
   print('Dien tich tam giac la: ', Tinh_dien_tich_tam_giac(a,b,c))