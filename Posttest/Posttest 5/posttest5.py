print("=" * 55)
print("     PROGRAM PEMBAGIAN TAKJIL")
print("=" * 55)

data_takjil = []
counter = 1

while True:
    print("\n" + "-" * 55)
    print("MENU: 1.Tambahkan  2.Membaca  3.Perbarui  4.Hapus  5.Keluar")
    print("-" * 55)
    
    pilihan = input("Pilih menu: ")
    
    if pilihan == "1":
        print("\n-- TAMBAH DATA BARU --")
        
        tanggal = input("Tanggal : ")
        waktu   = input("Waktu   : ")
        lokasi  = input("Lokasi  : ")
        jenis   = input("Jenis   : ")
        jml_inp = input("Jumlah  : ")
        pj      = input("PJ      : ")
        
        if jml_inp.isdigit():
            jumlah = int(jml_inp)
        else:
            jumlah = 0
        
        data_baru = (counter, tanggal, waktu, lokasi, jenis, jumlah, pj)
        data_takjil.append(data_baru)
        
        print("Data No.", counter, "ditambahkan!")
        counter = counter + 1
    
    elif pilihan == "2":
        print("\n-- DAFTAR DATA --")
        
        if len(data_takjil) == 0:
            print("Data kosong.")
        else:
            print("-" * 65)
            print(f"{'No':<3} {'Tgl':<10} {'Wkt':<6} {'Lokasi':<14} {'Jenis':<10} {'Jml':<4} {'PJ'}")
            print("-" * 65)
            
            i = 0
            while i < len(data_takjil):
                d = data_takjil[i]
                print(d[0], "", d[1], "", d[2], "", d[3], "", d[4], "", d[5], "", d[6])
                i = i + 1
            
            print("-" * 65)
            print("Total:", len(data_takjil), "data")

    elif pilihan == "3":
        print("\n-- UBAH DATA --")
        
        if len(data_takjil) == 0:
            print("Data kosong.")
        else:
            print("\nDaftar:")
            i = 0
            while i < len(data_takjil):
                d = data_takjil[i]
                print("  [", i+1, "]", d[0], "|", d[1], "|", d[3], "|", d[4])
                i = i + 1
            
            inp = input("\nPilih nomor yang diubah: ")
            
            if inp.isdigit():
                no = int(inp)
                
                if no >= 1 and no <= len(data_takjil):
                    idx = no - 1

                    old = data_takjil[idx]
                    
                    print("\nData saat ini:")
                    print("  1. Tanggal :", old[1])
                    print("  2. Waktu   :", old[2])
                    print("  3. Lokasi  :", old[3])
                    print("  4. Jenis   :", old[4])
                    print("  5. Jumlah  :", old[5])
                    print("  6. PJ      :", old[6])
                    
                    print("\nMasukkan nilai BARU (tekan Enter jika tidak diubah):")

                    new_tgl = input("  Tanggal baru [" + old[1] + "]: ")
                    new_wkt = input("  Waktu baru   [" + old[2] + "]: ")
                    new_lok = input("  Lokasi baru  [" + old[3] + "]: ")
                    new_jns = input("  Jenis baru   [" + old[4] + "]: ")
                    new_jml = input("  Jumlah baru  [" + str(old[5]) + "]: ")
                    new_pj  = input("  PJ baru      [" + old[6] + "]: ")

                    if new_tgl == "":
                        final_tgl = old[1]
                    else:
                        final_tgl = new_tgl
                    
                    if new_wkt == "":
                        final_wkt = old[2]
                    else:
                        final_wkt = new_wkt
                    
                    if new_lok == "":
                        final_lok = old[3]
                    else:
                        final_lok = new_lok
                    
                    if new_jns == "":
                        final_jns = old[4]
                    else:
                        final_jns = new_jns
                    
                    if new_jml == "":
                        final_jml = old[5]
                    elif new_jml.isdigit():
                        final_jml = int(new_jml)
                    else:
                        final_jml = old[5]
                    
                    if new_pj == "":
                        final_pj = old[6]
                    else:
                        final_pj = new_pj

                    data_baru = (old[0], final_tgl, final_wkt, final_lok, final_jns, final_jml, final_pj)
                    data_takjil[idx] = data_baru
                    
                    print("\nData BERHASIL diubah!")
                    print("    Verifikasi:", data_takjil[idx])
                    
                else:
                    print("Nomor tidak valid.")
            else:
                print("Input harus angka.")

    elif pilihan == "4":
        print("\n-- HAPUS DATA --")
        
        if len(data_takjil) == 0:
            print("Data kosong.")
        else:
            i = 0
            while i < len(data_takjil):
                d = data_takjil[i]
                print("  [", i+1, "]", d[0], "|", d[1], "|", d[3])
                i = i + 1
            
            inp = input("\nPilih nomor yang dihapus: ")
            
            if inp.isdigit():
                no = int(inp)
                
                if no >= 1 and no <= len(data_takjil):
                    idx = no - 1
                    konfirmasi = input("Yakin hapus? (y): ")
                    
                    if konfirmasi == "y":
                        data_takjil.pop(idx)
                        print("Data terhapus.")
                else:
                    print("Nomor tidak valid.")
            else:
                print("Input harus angka.")

    elif pilihan == "5":
        print("\nTerima kasih!")
        break
    
    else:
        print("Pilih 1-5.")

print("Program selesai.")