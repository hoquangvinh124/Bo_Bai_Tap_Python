# Bai tap 74
def word_form(n):
    hang_chuc = (n // 10) % 10
    hang_don_vi = n % 10

    match hang_don_vi:
        case 0 if hang_chuc > 0:
            hang_don_vi = ''
        case 0 if hang_chuc == 0:
            hang_don_vi = 'không'
        case 1 if hang_chuc <= 1:
            hang_don_vi = 'một'
        case 1 if hang_chuc > 1:
            hang_don_vi = 'mốt'
        case 2:
            hang_don_vi = 'hai'
        case 3:
            hang_don_vi = 'ba'
        case 4:
            hang_don_vi = 'bốn'
        case 5 if hang_chuc == 0:
            hang_don_vi = 'năm'
        case 6:
            hang_don_vi = 'sáu'
        case 7:
            hang_don_vi = 'bảy'
        case 8:
            hang_don_vi = 'tám'
        case 9:
            hang_don_vi = 'chín'
        case 5 if hang_chuc > 0 and hang_don_vi == 5:
            hang_don_vi = 'lăm'

    match hang_chuc:
        case 0:
            hang_chuc = ''
        case 1:
            hang_chuc = 'Mười '
        case 2:
            hang_chuc = 'Hai mươi '
        case 3:
            hang_chuc = 'Ba mươi '
        case 4:
            hang_chuc = 'Bốn mươi '
        case 5:
            hang_chuc = 'Năm mươi '
        case 6:
            hang_chuc = 'Sáu mươi '
        case 7:
            hang_chuc = 'Bảy mươi '
        case 8:
            hang_chuc = 'Tám mươi '
        case 9:
            hang_chuc = 'Chín mươi '

    return str(hang_chuc) + str(hang_don_vi)

n = int(input('Nhập một số nguyên dương có 2 chữ số: '))
print(word_form(n))
