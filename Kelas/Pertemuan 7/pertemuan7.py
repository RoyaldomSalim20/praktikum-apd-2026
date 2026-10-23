#def luas_persegi_panjang():
#    luas = 3 * 5
#    return luas

#print("Luas persegi panjang", luas_persegi_panjang())

#def luas_persegi(panjang, lebar):
#    luas = panjang * lebar
#    return luas

#print("Luas persegi:", luas_persegi(7, 5))

#def luas_persegi_panjang(panjang, lebar):
#    luas = panjang * lebar
#    return luas
#def total_harga_tanah(panjang, lebar, harga = 100000):
#    total = luas_persegi_panjang(panjang, lebar) * harga
#    return total

#print("Luas persegi panjang:", luas_persegi_panjang(7, 4))
#print("Total harga tanah:", total_harga_tanah(7, 4))

#def pengumuman(matkul):
#    print(f"Hari ini Pengujian Proyek Akhir {matkul}")

#pengumuman("APD")

#def perkenalan():
#    nama = input("Masukkan nama anda: ")

#perkenalan()

#def sapa_pengguna(nama_pengguna):
#    print(f"Halo, selamat datang {nama_pengguna}")

#sapa_pengguna("Citra")

#nama = "Larry"
#prodi = "Informatika"

#def data():
#    nama = "Teknik Kedokteran"
#    prodi = "Kedokteran Lanjut"
#    print("Nama:", nama)
#    print("Prodi:", prodi)

#data()

#print("Nama:", nama)
#print("Prodi:", prodi)

#def faktorial(n):

#    if n == 0 or n == 1:
#        return 1
#    else:
#        return n * faktorial(n - 1)

#hasil_faktorial = faktorial(4)
#print(f"Hasil dari 4! {hasil_faktorial}")

#def hitung_mundur(n):
#    if n == 0:
#        print("Selesai")
#    else:
#        print(n)
#        hitung_mundur(n-1)

#hitung_mundur(5)

#umur = input("Masukkan umur anda: ")
#print(umur)

try:
    umur = int(input("Masukkan Umur Anda: "))
    if umur < 17:
        raise ValueError("Anda masuk kategori bocil")
    if umur > 17:
        raise ValueError("Anda sudah Dewasa")
except ValueError as e:
    print(e)
#    print("Umur yang dimasukkan tidak sesuai dengan nilai")
else:
    print(f"Umur anda adalah {umur}")
finally:
    print("Program selesai")