#Bai tap 81


r = int(input('Nhap Revenue: '))
c = int(input('Nhap Cost: '))


def ROI(r,c):
   return (r-c)/c

def Investment(ROI):
   match ROI:
       case ROI if ROI >= 0.75:
           print('Dau tu')
       case _:
           print('Khong dau tu')


print('Ti le ROI: ',ROI(r,c))
Investment(ROI(r,c))
