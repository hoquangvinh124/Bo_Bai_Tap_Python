A=float(input('Số tiền gốc ban đầu: '))
r=float(input('Lãi suất tháng (r%): '))
N=int(input('Số năm tiết kiệm: '))


def tinhtienlai(A,r,N):
   tienlai=0
   sothang=12*N
   for i in range(1,sothang+1):
       tienlai+=(A*r)/100
       if i % 3 == 0:
           A+=tienlai
           tienlai=0
   A=round(A, -3)
   return f'{A:,.0f}'


print(tinhtienlai(A, r, N))
