#Bai tap 56
math=float(input("Diem Toan: "))
physics=float(input("Diem Vat Ly: "))
chemistry=float(input("Diem Hoa Hoc: "))
def AVG(math, physics, chemistry):
   avg = (math + physics + chemistry) / 3
   lam_tron = round(avg, 2)
   return lam_tron
print("Diem trung binh=", AVG(math, physics, chemistry))

