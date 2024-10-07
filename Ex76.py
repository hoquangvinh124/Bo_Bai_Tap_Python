day=int(input('Ngày: '))
month=int(input('Tháng: '))
year=int(input('Năm: '))


def namnhuan(year):
   return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def ngaytrongthang(month, year):
   if month in (1, 3, 5, 7, 8, 10, 12):
       return 31
   elif month in (4, 6, 9, 11):
       return 30
   elif month == 2:
       return 29 if namnhuan(year) else 28


if day < ngaytrongthang(month, year):
   day += 1
else:
   day = 1
   if month == 12:
       month = 1
       year += 1
   else:
       month += 1


print(f'{day}/{month}/{year}')
