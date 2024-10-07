#Bai tap 55

def Doi_format_gio(t):
   hour=(t//3600)%24
   minute=(t%3600)//60
   second=(t%3600)%60
   format_12_gio = hour % 12 if hour != 0 else 12
   format_AM_va_PM = 'AM' if hour < 12 else "PM"
   return print(f'{format_12_gio}:{minute}:{second} {format_AM_va_PM}')


t=int(input("Nhập số giây: "))
Doi_format_gio(t)
