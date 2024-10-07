#Bai tap 105


while True:
   n=int(input("Nhap so nguyen duong: "))
   so_lan_dem = 0 #Vi so nguyen to la so chia het cho 1 va chinh no
   for i in range(1,n+1):
       if n % i == 0:
           so_lan_dem+=1
   if so_lan_dem == 2:
       print(f'{n} la so nguyen to')
   else:
       print(f'{n} khong phai la so nguyen to')
   ask=input("Tiep tuc ? (y/n) :")
   if ask == 'n':
       break
print('Tam biet!')




