def xacdinhquy():
   try:
       month = int(input("Nhập vào một tháng: "))
       if 1 <= month <= 12:
           match month:
               case 1 | 2 | 3:
                   return print("Tháng thuộc quý 1.")
               case 4 | 5 | 6:
                   return print("Tháng thuộc quý 2.")
               case 7 | 8 | 9:
                   return print("Tháng thuộc quý 3.")
               case 10 | 11 |12:
                   return print("Tháng thuộc quý 4.")
       else:
           return print("Tháng không hợp lệ.")
   except ValueError:
       print("Vui lòng nhập một số nguyên hợp lệ!")


xacdinhquy()

