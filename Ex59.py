#Bai tap 59
import math


a = int(input('a: '))
x = int(input('x: '))


if x > 0 and a > 0 and a != 1:
   ket_qua = math.log(x) / math.log(a)
   print(f"log{a}({x}) = {ket_qua}")
else:
   print("a hoac x khong hop le!")


