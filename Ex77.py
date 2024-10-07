try:
   a=float(input('a: '))
   b=float(input('b: '))
   c=str(input('op:'))


   match (a,b,c):
       case (a, b, c) if c == '+':
           print(f'{a}{c}{b}={a+b}')
       case (a, b, c) if c == '-':
           print(f'{a}{c}{b}={a-b}')
       case (a, b, c) if c == '*':
           print(f'{a}{c}{b}={a*b}')
       case (a, b, c) if c == '/' and b != 0:
           print(f'{a}{c}{b}={a/b}')
       case (a, b, c) if c == '/' and b == 0:
           print('Lỗi chia cho 0!')
       case _:
           print('Toán tử không hợp lệ!')

except ValueError:
   print('Vui lòng nhập giá trị hợp lệ!')
