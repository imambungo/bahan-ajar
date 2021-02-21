# buatlah program yang menerima input nilai mk
# 0-50, kasih nilai D
# 51-70, kasih nilai C
# 71-80, kasih nilai B
# 81-100, kasih nilai A
# kalau angkanya < 0 atau angkanya > 100, outputkan "tidak valid"

angka = input('masukkan angka nilai: ') # string
angka = float(angka) # int

if angka >= 81 and angka <= 100:
    print('anda dapat A')
elif angka >= 71 and angka <= 80: # else if
    print('anda dapat B')
elif angka >= 51 and angka <= 70: # else if
    print('anda dapat C')
elif angka >= 0 and angka <= 50: # else if
    print('anda dapat D')
else:
    print('input tidak valid')


if angka < 0 or angka > 100:
    print('input tidak valid')
elif angka >= 81:
    print('anda dapat A')
elif angka >= 71:
    print('anda dapat B')
elif angka >= 51:
    print('anda dapat C')
else:
    print('anda dapat D')