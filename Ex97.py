"""
Giá trị ban đầu: m=2, n=26, a=3, b=10
Sau đó hàm calculate sẽ nhận đối số (m,n,a,b) lần lượt là 2,26,3,10
Vòng lặp thứ nhất: for i in range(m, n+1):
Với mỗi giá trị i từ m đến n (bao gồm cả n), chương trình sẽ thực hiện:
    Kiểm tra xem căn bậc hai của i có phải là số nguyên hay không. Nếu có thì c = True, nếu không thì c = False.
    Nếu c = True:
        Nếu i nằm trong khoảng từ a đến b và là số chẵn, chương trình sẽ bỏ qua vòng lặp hiện tại.
        Nếu không thỏa mãn điều kiện trên, chương trình cộng giá trị i vào s1.
    Nếu c = False:
        Thực hiện một vòng lặp: for j in range(1, i)
            Kiểm tra j có chia hết cho i và j là số chẵn. Nếu đúng, giá trị j được cộng vào s2.

Sau khi hoàn thành, hàm trả về hai giá trị s1 và s2.

==> x=50, y=84
"""
from math import sqrt, pow

def calculate(m, n, a, b):
    s1 = s2 = 0
    for i in range(m, n+1):
        c = True if sqrt(i) % 1 == 0 else False
        if c:
            if a <= i <= b and i % 2 == 0:
                continue
            else:
                s1 += i
        else:
            for j in range(1, i):
                if i % j == 0 and j % 2 == 0:
                    s2 += j
    return s1, s2

m = 2
n = m**3*3 + 2
a = int(sqrt(n)) - 2
b = pow(a, 2) + 1
print(f"m = {m}, n = {n}, a = {a}, b = {b}")
x, y = calculate(m, n, a, b)
print("x = {}, y = {}".format(x, y))
