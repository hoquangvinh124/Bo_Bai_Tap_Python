#Bai tap 69

year = int(input("Vui long nhap nam: "))

def KiemTraNamNhuan(year):
   if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
       return True
   else:
       return False


if KiemTraNamNhuan(year) == True:
   print(f'{year} la nam nhuan')
else:
   print(f'{year} la nam khong nhuan')




