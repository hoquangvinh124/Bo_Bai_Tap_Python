#Bai tap 60
n = int(input('Nhap mot so nguyen duong co 3 chu so: '))


hang_tram = n // 100
hang_chuc = (n // 10) % 10
hang_don_vi = n % 10
so_moi = (hang_don_vi*100) + (hang_chuc*10) + (hang_tram)


print(so_moi)
