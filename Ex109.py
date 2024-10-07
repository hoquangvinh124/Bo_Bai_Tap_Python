pp = float(input('Giá mua mới: '))
t = float(input('Phí vận chuyển: '))
ld = float(input('Phí lắp đặt: '))
snsd = int(input('Số năm sử dụng dự kiến: '))


ad=0
i=0
opofa= pp + ld + t
adr = opofa / snsd
mdr = adr/12


print('Nguyên giá tài sản cố định:', int(opofa))
print('Mức trích khấu hao hàng năm:', int(adr))
print('Mức trích khấu hao hàng tháng:', int(mdr))


while (i<snsd):
   ad = adr * (i+1)
   fpdr = opofa - ad
   i+=1
   print(f'Năm {i}, Sau khấu hao còn:', int(fpdr))
