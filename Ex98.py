#Bai tap 98
from random import randrange


while True:
   mn = randrange(1,101)
   chien_thang=False
   so_lan = 0
   while so_lan < 7:
       pn = int(input('Nhap so cua ban nao: '))
       if mn == pn:
           print('Chuc mung ban da thang tro choi!')
           chien_thang=True
           break
       elif mn < pn:
           print('So cua ban lon hon so cua may tinh')
           so_lan+=1
       elif mn > pn:
           print('So cua ban nho hon so cua may tinh')
           so_lan += 1

   if chien_thang==False:
       print('Tro choi ket thuc! So cua may tinh',mn)
   ask = input("Tiep tuc chu?(y/n)")
   if ask == 'n':
       break


print("Cam on vi da choi voi chung toi!")

