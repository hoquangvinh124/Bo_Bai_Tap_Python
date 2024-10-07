#Bai tap 54
import math
try:
    def tinh_chu_vi(r):
        perimeter=2*math.pi*r
        return print("Chu vi hinh tron: ", perimeter)
    def tinh_dien_tich(r):
        area =r**2
        return print("Dien tich hinh tron: ", area)
    r=float(input("Nhap ban kinh: "))
    tinh_chu_vi(r)
    tinh_dien_tich(r)
except:
    print("Error!")

