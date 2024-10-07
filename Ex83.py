#Bai tap 83

A = float(input("Old kilowatt-hour number: "))
B = float(input("New kilowatt-hour number: "))
C = float(input("The number of households sharing the same electricity meter: "))

def kiemtra(A,B):
    if A > B or A < 0 or B < 0:
        print('Vui long nhap gia tri hop le!')
        return False

def Laddered_cost_of_living(A, B, C):
   if B-A <= 50*C:
       pay = (B-A) * 1484
   elif B-A <=100*C:
       pay = (50*C * 1484) + ((B-A) - 50*C) * 1533
   elif B-A <=200*C:
       pay = (50*C*1484) + (50*C*1533) + ((B-A) - 100*C) * 1786
   elif B-A <=300*C:
       pay = (50*C*1484) + (50*C*1533) + (100*C*1786) + ((B-A) - 200*C) * 2242
   elif B-A <=400*C:
       pay = (50*C*1484) + (50*C*1533) + (100*C*1786) + (100*C*2242) + ((B-A) - 300*C) * 2503
   else:
       pay = (50*C*1484) + (50*C*1533) + (100*C*1786) + (100*C*2242) + (100*C*2503) + ((B-A) - 400*C) * 2587
   if C==0:
        return
   else:
        return print('Laddered cost of living: ',pay )


def Business_electricity_price(A, B):
   pay = (B-A)*2320
   return print('Business electricity price ',pay )


def Electricity_production_price(A, B):
   pay = (B-A)*1518
   return print('Electricity production price: ',pay )


if kiemtra(A,B) != False:
    Laddered_cost_of_living(A, B, C)
    Business_electricity_price(A, B)
    Electricity_production_price(A, B)



