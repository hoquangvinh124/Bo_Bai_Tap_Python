"""
function kiemtra(n):  def chứ không phải function
    if (n%2 ==1):     Lỗi logic: Chương trình chỉ nhận số lẻ và không nhận số chẵn
        S=0
        for i in range (1,n/2+1):       (1,n//2+1) --> Đảm bảo rằng phép chia luôn nguyên tránh gây lỗi cho vòng lặp
            if (n%i==0):
                S=S+i
        if (S=n):                  S==n
            return 1
    return 0

n =input ('Input n')   n = int(input('Input n: ')) --> Đảm bảo rằng chỉ nhận số nguyên
for i in range (1,n+1):
    if (kiemtra(i)==1):
        print (i)

==> Chương trình kiểm tra xem số nguyên n có phải là số hoàn hảo hay không
Hàm kiemtra(n) trả về 1 nếu n là số hoàn hảo và 0 nếu không phải là số hoàn hảo
Sau đó, chương trình in ra tất cả các số hoàn hảo từ 1 đến n
"""

def kiemtra(n):
    S = 0
    for i in range(1, n // 2 + 1):
        if (n % i == 0):
            S += i
    if (S == n):
        return 1
    return 0

n = int(input('Input n: '))
for i in range(1, n + 1):
    if (kiemtra(i) == 1):
        print(i)



