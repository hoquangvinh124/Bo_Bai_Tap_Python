#Bai tap 82

def Tien_dien():
    try:
        Ten = input("Vui long nhap ten khach hang: ")
        Nhom_Khach_Hang = int(input("Nhom khach hang: "))
        So_kWh_su_dung = float(input("So kWh su dung: "))
        EP=0
        if So_kWh_su_dung<0:
            print("So kWh su dung khong hop le!")
            return 2
        if Nhom_Khach_Hang == 1:
           if 0<=So_kWh_su_dung<=50:
               EP = 1549
           elif 51 <= So_kWh_su_dung <= 100:
               EP = 1600
           elif 101 <= So_kWh_su_dung <= 200:
               EP = 1858
           elif 201 <= So_kWh_su_dung <= 300:
               EP = 2340
           elif 301 <= So_kWh_su_dung <= 400:
               EP = 2615
           elif So_kWh_su_dung >= 401:
               EP = 2701
        elif Nhom_Khach_Hang == 2:
           EP = 2271
        else:
           print("Nhom khach hang khong hop le!")
           return 1
        cost = EP * So_kWh_su_dung
        print(f"\nXin chao {Ten} ")
        print("Nhom khach hang: ", Nhom_Khach_Hang)
        print("Tien dien thang nay: ", cost)
    except:
        print('Đã xảy ra lỗi!')

Tien_dien()






