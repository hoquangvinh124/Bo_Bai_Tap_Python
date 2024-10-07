from math import factorial


t=int(input('Nhập số người dương tính với virus COVID-19: '))
r=int(input('Nhập số nguời đã hồi phục: '))


def tinhxacsuat(t,r):
   if r > t:
       return "Lỗi: Số người hồi phục không thể lớn hơn tổng số người."
   ct=t-r
   es=factorial(t)
   kqtl=ct*factorial(t-1)
   p=kqtl/es
   return f'{p*100:.2f}%'


print(tinhxacsuat(t,r))

