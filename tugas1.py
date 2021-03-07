ipk = float(input('masukkan ipk: '))

if (ipk < 0 and ipk > 4):
    print('input tidak valid')
elif (ipk < 2.76):
    print('anda tidak lulus')
elif (ipk >= 2.76 and ipk <= 3):
    print('predikat: memuaskan')
elif (ipk > 3 and ipk <= 3.5):
    print('predikat: sangat memuaskan')
else:
    semester = int(input('masukkan masa studi (semester): '))
    if (semester <= 8):
        jumlah_nilai_c = int(input('masukkan jumlah nilai c: '))
    if (semester <= 8 and jumlah_nilai_c <= 1):
        nilai_skripsi = input('masukkan nilai skripsi: ')
    if (semester <= 8 and jumlah_nilai_c <= 1 and nilai_skripsi == 'A'):
        print('predikat: cumlaude')
    else:
        print('predikat: sangat memuaskan')