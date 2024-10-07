def TinhSoNgayTrongThang(month):
    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            return 31
        case 4 | 6 | 9 | 11:
            return 30
        case 2:
            year = int(input('Vui long nhap nam: '))
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                return 29
            else:
                return 28
        case _:
            print('Thang khong hop le')

try:
    month = int(input("Vui long nhap thang: "))
    print(f'Thang {month} co', TinhSoNgayTrongThang(month), 'ngay')
except ValueError:
    print('Vui long nhap gia tri hop le!')
