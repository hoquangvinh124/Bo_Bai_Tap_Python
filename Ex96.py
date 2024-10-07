"""
i > N chỉ có một số thỏa mãn là 9
ở hàm calculate N = 9. Ở trong vòng lặp while (i <= N), i chia hết cho 3 chỉ có: 3, 6, 9
Nên kết quả là: S = 1 * 3 * 6 * 9 = 162
"""


def calculate(N):
    S = 1
    i = 1
    while (i <= N):
        if (i % 3 == 0):
            S *= i
        i += 1
    return S

N = 8
for i in range(1, 10):
    if (i > N):
        print('====' + str(calculate(i)))
