usia = input('masukkan usia: ')

terlalu_muda = int(usia) < 18
terlalu_tua = int(usia) > 40
if terlalu_muda:
    print('tidak boleh masuk')
elif terlalu_tua:
    print('anda ketuaan')
else:
    print('silahkan masuk')

print('program selesai')