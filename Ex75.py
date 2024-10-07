
def word_form(n):
   hang_chuc = (n // 10) % 10
   hang_don_vi = n % 10

   if hang_chuc == 1:
       match hang_don_vi:
           case 0:
               return 'Ten'
           case 1:
               return 'Eleven'
           case 2:
               return 'Twelve'
           case 3:
               return 'Thirteen'
           case 4:
               return 'Fourteen'
           case 5:
               return 'Fifteen'
           case 6:
               return 'Sixteen'
           case 7:
               return 'Seventeen'
           case 8:
               return 'Eighteen'
           case 9:
               return 'Nineteen'

   match hang_don_vi:
       case 0 if hang_chuc > 0:
           hang_don_vi = ''
       case 0 if hang_chuc == 0:
           hang_don_vi = 'zero'
       case 1:
           hang_don_vi = 'one'
       case 2:
           hang_don_vi = 'two'
       case 3:
           hang_don_vi = 'three'
       case 4:
           hang_don_vi = 'four'
       case 5:
           hang_don_vi = 'five'
       case 6:
           hang_don_vi = 'six'
       case 7:
           hang_don_vi = 'seven'
       case 8:
           hang_don_vi = 'eight'
       case 9:
           hang_don_vi = 'nine'

   match hang_chuc:
       case 0:
           hang_chuc = ''
       case 2:
           hang_chuc = 'Twenty' if hang_don_vi == '' else 'Twenty-'
       case 3:
           hang_chuc = 'Thirty' if hang_don_vi == '' else 'Thirty-'
       case 4:
           hang_chuc = 'Forty' if hang_don_vi == '' else 'Forty-'
       case 5:
           hang_chuc = 'Fifty' if hang_don_vi == '' else 'Fifty-'
       case 6:
           hang_chuc = 'Sixty' if hang_don_vi == '' else 'Sixty-'
       case 7:
           hang_chuc = 'Seventy' if hang_don_vi == '' else 'Seventy-'
       case 8:
           hang_chuc = 'Eighty' if hang_don_vi == '' else 'Eighty-'
       case 9:
           hang_chuc = 'Ninety' if hang_don_vi == '' else 'Ninety-'

   return str(hang_chuc) + str(hang_don_vi)

n = int(input('Input a positive number with maximum 2 digits: '))

print(word_form(n))
