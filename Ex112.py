A1 = float(input("Nhập xác suất có kiểm tra sức khỏe: "))
A2 = float(input("Nhập xác suất không kiểm tra sức khỏe: "))
BA1 = float(input("Nhập xác suất không có vấn đề sức khỏe nếu có kiểm tra sức khỏe: "))
BA2 = float(input("Nhập xác suất không có vấn đề sức khỏe nếu không kiểm tra sức khỏe: "))


def tinhxacsuat(A1,A2,BA1,BA2):
   B = BA1 * A1 + BA2 * A2
   return f'{B*100:,.2f}%'


print(tinhxacsuat(A1, A2, BA1, BA2))
