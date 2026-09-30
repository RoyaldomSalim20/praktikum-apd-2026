print("Login")

Nama = "Salim"
NIM = "103"

Nama_input = input("Masukkan nama panggilan: ")
NIM_input = input("Masukkan 2-3 digit terakhir NIM: ")

if Nama_input == Nama and NIM_input == NIM:
    print("Login berhasil!")
    print(f"Selamat datang, {Nama_input}!")
    
    print("\nPilih jenis konsol:")
    print("1. PS4        : Rp 10.000/jam")
    print("2. PS4 Pro    : Rp 15.000/jam")
    print("3. PS5        : Rp 20.000/jam")
    
    pilihan_konsol = int(input("Masukkan pilihan (1-3): "))
    
    if pilihan_konsol == 1:
        nama_konsol = "PS4"
        harga_per_jam = 10000
    elif pilihan_konsol == 2:
        nama_konsol = "PS4 Pro"
        harga_per_jam = 15000
    elif pilihan_konsol == 3:
        nama_konsol = "PS5"
        harga_per_jam = 20000
    else:
        print("Pilihan tidak valid!")
        exit()
    
    jumlah_jam = int(input(f"Masukkan jumlah jam sewa untuk {nama_konsol}: "))
    
    if jumlah_jam <= 0:
        print("Jumlah jam harus lebih dari 0.")
        exit()
    
    total_harga = harga_per_jam * jumlah_jam
    
    persen_diskon = 0
    diskon_durasi = 0
    
    if jumlah_jam >= 5:
        persen_diskon = 8
        diskon_durasi = total_harga * 0.08
    elif jumlah_jam >= 3:
        persen_diskon = 5
        diskon_durasi = total_harga * 0.05
    else:
        persen_diskon = 0
        diskon_durasi = 0

    total_bayar = total_harga - diskon_durasi

print("\n" + "=" * 50)
print("       STRUK TRANSAKSI RENTAL PS")
print("=" * 50)
print(f"Nama Penyewa     : {Nama_input}")
print(f"NIM              : ***{NIM_input}")
print(f"Total Bayar      : Rp {total_bayar:,}")
print("=" * 50)
print(f"Diskon ({persen_diskon}%)       : -Rp {diskon_durasi:,}")
print(f"Total Harga      : Rp {total_harga:,}")
print("=" * 50)
print(f"Jenis Konsol     : {nama_konsol}")
print(f"Harga/Jam        : Rp {harga_per_jam:,}")
print(f"Jumlah Jam       : {jumlah_jam} jam")
print("=" * 50)
print("\nTerima kasih telah bermain di Rental PS kami!")