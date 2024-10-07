#Bai tap 21
paint_cans = int(input("Nhap so luong hop son: "))

Price = 350000 * paint_cans
Hats = paint_cans // 3
Pens = 0
if paint_cans >= 3:
    Pens = (paint_cans % 3) * 2


print("Don gia: ", Price)
if Hats == 0 and Pens == 0:
   print("Ban khong duoc trung thuong")
else:
   print(f"Ban duoc thuong them {Hats} cai mu va {Pens} cay but")
