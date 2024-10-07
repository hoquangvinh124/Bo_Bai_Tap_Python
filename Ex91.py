"""
a) in từ 0 đến 4 với bước nhảy là 1
b) in từ 5 đến 9 với bước nhảy là 1
c) in từ 5 đến 17 với bước nhảy là 3
d) in từ 20 đến 6 với bước nhảy -1
e) in từ 20 đến 8 với bước nhảy -3
f) từ 10 đến 5 với bước nhảy là 1 --> không in
g) dải số bắt đầu từ 0 với bước nhảy 1 ---> không có số nào để in ---> không in
h) in từ 10 đến 100 với bước nhảy 10
i) in từ 10 đến 0 với bước nhảy -1
j) in từ -3 đến 3 với bước nhảy là 1
k) in từ 0 đến 9 với bước nhảy là 1
"""

print(list(range(5)))           # (a)
print(list(range(5, 10)))       # (b)
print(list(range(5, 20, 3)))    # (c)
print(list(range(20, 5, -1)))   # (d)
print(list(range(20, 5, -3)))   # (e)
print(list(range(10, 5)))       # (f)
print(list(range(0)))           # (g)
print(list(range(10, 101, 10))) # (h)
print(list(range(10, -1, -1)))  # (i)
print(list(range(-3, 4)))       # (j)
print(list(range(0, 10, 1)))    # (k)
