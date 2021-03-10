from math import pi
print ('Tugas 2 Praktek Pemrograman Komputer Menyusun Rumus')
print ('========================================================')

print ('Ingin menghitunng apakah anda?')
print ('1. Luas persegi panjang')
print ('2. Luas lingkaran')
print ('3. Luas kubus')
print ('4. Konversi suhu celcius ke fahrenheit')
print ('5. Konversi suhu reamur ke kelvin')

choice = input('Masukkan hitungan pilihan anda (1/2/3/4/5)')

if choice == '1':
    panjang = float(input('Masukkan panjang: '))
    lebar = float(input('Masukkan lebar: '))
    Luas = panjang*lebar

    print ('Luas persegi panjangnya adalah %s'%Luas)
    cetak = 1

elif choice == '2':
    Radius = float(input('Masukkan jari-jari: '))
    Luas = pi*Radius

    print ('Luas lingkarannya adalah %s'%Luas)
    cetak = 1

elif choice == '3':
    Rusuk = float(input('Masukkan panjang rusuk: '))
    Luas = (Rusuk**2)

    print ('Luas permukaan kubusnya adalah %s'%Luas)
    cetak = 1

elif choice == '4':
    Celcius = float(input('Masukkan suhu dalam celsius untuk diubah ke fahrenheit: '))
    Rumus = ((9/5)*Celcius)+32

    print ('Suhu dalam fahrenheit sebesar %s'%Rumus)
    cetak = 1

elif choice == '5':
    Reamur = float(input('Masukkan suhu dalam reamur untuk diubah ke kelvin: '))
    Rumus = (((5/4)*Reamur)+273)

    print ('Suhu dalam kelvin sebesar %s'%Rumus)
    cetak = 1

else :
    print ('Error System')