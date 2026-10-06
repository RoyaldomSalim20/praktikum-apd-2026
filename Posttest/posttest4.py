USERNAME_BENAR = "Salim"
PASSWORD_BENAR = "103"

uang_bulanan = 0
total_pengeluaran = 0

print("=" * 50)
print("    SISTEM REKAPITULASI PENGGUNAAN UANG SAKU")
print("=" * 50)

percobaan_login = 3
login_berhasil = False

while percobaan_login > 0:
    print(f"\n--- HALAMAN LOGIN (Sisa Percobaan: {percobaan_login}) ---")
    
    username_input = input("Masukkan Username: ")
    password_input = input("Masukkan Password (3 digit NIM): ")
    
    if username_input == USERNAME_BENAR and password_input == PASSWORD_BENAR:
        print("\nLogin Berhasil!")
        print("=" * 50)
        login_berhasil = True
        break
    else:
        percobaan_login = percobaan_login - 1
        if percobaan_login > 0:
            print(f"\nLogin Gagal. Sisa percobaan: {percobaan_login}")
        else:
            print("\n" + "!" * 50)
            print("  ERROR: PERCOBAAN LOGIN HABIS!")
            print("  Akun Anda telah diblokir sementara.")
            print("  Silakan hubungi administrator.")
            print("!" * 50)

if not login_berhasil:
    print("\nProgram dihentikan karena gagal login 3 kali.")
    exit()

print("\n--- INISIALISASI UANG SAKU ---")

input_uang = input("Masukkan jumlah uang saku bulanan (Rp): ")

if input_uang.isdigit():
    uang_bulanan = int(input_uang)
else:
    uang_bulanan = 2500000

total_pengeluaran = 0

print(f"\n✓ Uang saku bulanan berhasil diinisialisasi: Rp {uang_bulanan:,}")
print(f"✓ Total pengeluaran awal: Rp {total_pengeluaran:,}")

print("\n" + "=" * 50)
print("         MENU UTAMA PROGRAM")
print("=" * 50)

while True:
    if uang_bulanan <= 0:
        print("\nPERINGATAN: Saldo uang saku Anda habis!")
        print("Program akan dihentikan.")
        break
    
    print("\n┌─────────────────────────────────────┐")
    print("│           PILIHAN MENU              │")
    print("├─────────────────────────────────────┤")
    print("│ [1] Catat Pengeluaran               │")
    print("│ [2] Cek Sisa Uang Saku              │")
    print("│ [3] Keluar                          │")
    print("└─────────────────────────────────────┘")
    
    pilihan = input("\nPilih menu (1-3): ")
    
    if pilihan == "1":
        print("\n" + "-" * 40)
        print("       CATAT PENGGELUARAN BARU")
        print("-" * 40)
        
        while True:
            if uang_bulanan <= 0:
                print("\nSaldo tidak mencukupi untuk pengeluaran lagi!")
                break
            
            print(f"\nSaldo saat ini: Rp {uang_bulanan:,}")
            nominal_str = input("Masukkan nominal pengeluaran (Rp): ")
            
            if nominal_str.isdigit():
                nominal = int(nominal_str)
                
                if nominal <= 0:
                    print("Nominal harus lebih dari 0!")
                elif nominal > uang_bulanan:
                    print(f"Nominal melebihi saldo! Maksimal: Rp {uang_bulanan:,}")
                else:
                    uang_bulanan = uang_bulanan - nominal
                    total_pengeluaran = total_pengeluaran + nominal
                    
                    print(f"\nPengeluaran berhasil dicatat!")
                    print(f"  Nominal     : Rp {nominal:,}")
                    print(f"  Sisa Saldo  : Rp {uang_bulanan:,}")
                    
                    konfirmasi = input("\nApakah Anda ingin mencatat pengeluaran lagi? (Y/T): ")
                    konfirmasi_upper = konfirmasi.upper()
                    
                    if konfirmasi_upper == "Y":
                        continue
                    elif konfirmasi_upper == "T":
                        print("\nKembali ke Menu Utama...")
                        break
                    else:
                        print("Input tidak dikenal. Kembali ke Menu Utama...")
                        break
            else:
                print("Input tidak valid! Masukkan angka yang benar.")
    
    elif pilihan == "2":
        print("\n" + "=" * 40)
        print("      INFORMASI SALDO ANDA")
        print("=" * 40)
        print(f"  Uang Saku Awal   : Rp {uang_bulanan + total_pengeluaran:,}")
        print(f"  Total Pengeluaran: Rp {total_pengeluaran:,}")
        print(f"  ───────────────────────────────────")
        print(f"  Sisa Uang Saku   : Rp {uang_bulanan:,}")
        print("=" * 40)
        
        if (uang_bulanan + total_pengeluaran) > 0:
            persen_terpakai = (total_pengeluaran / (uang_bulanan + total_pengeluaran)) * 100
            print(f"  Persentase Terpakai: {persen_terpakai:.1f}%")
        elif pilihan == "3":
            print("\n" + "=" * 50)
            print("TERIMA KASIH TELAH MENGGUNAKAN PROGRAM INI")
            print("=" * 50)
            print(f"\n  Ringkasan Akhir:")
            print(f"  ├─ Total Pengeluaran : Rp {total_pengeluaran:,}")
            print(f"  └─ Sisa Uang Saku    : Rp {uang_bulanan:,}")
            print("\n Sampai jumpa lagi! \n")
        break
    
    else:
        print("\nPilihan tidak valid! Silakan pilih menu 1-3.")

print("\nProgram selesai.")