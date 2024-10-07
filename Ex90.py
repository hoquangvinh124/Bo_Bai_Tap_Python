"""
Xét b từ 0 đến 39 có 40 số: 20 số chẵn và 20 số lẻ
Xét a từ 0 đến 99 có: 50 số chẵn và 50 số lẻ
Theo logic vòng lặp có thể phân ra 2 trường hợp
TH1: số chẵn + số chẵn = số chẵn
TH2: số lẻ + số lẻ = số chẵn
==> TH1: 50*20=1000 dấu sao
    TH2: 50*20=1000 dấu sao
Tổng cộng = 1000 + 1000 = 2000 dấu sao
"""

a = 0
while a < 100:
    b = 0
    while b < 40:
        if (a + b) % 2 == 0:
            print('*', end='')
        b += 1
    print()
    a += 1
