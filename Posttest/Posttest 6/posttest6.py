
print("=" * 55)
print("     PROGRAM PEMBAGIAN TAKJIL")
print("=" * 55)

data_takjil = {}
counter = 1

while True:
    print("\n" + "-" * 55)
    print("MENU: 1.Tambahkan  2.Membaca  3.Perbarui  4.Hapus  5.Keluar")
    print("-" * 55)

    pilihan = input("Pilih menu: ")

    # CREATE
    if pilihan == "1":
        print("\n-- TAMBAH DATA BARU --")

        tanggal = input("Tanggal : ")
        waktu = input("Waktu   : ")
        lokasi = input("Lokasi  : ")
        jenis = input("Jenis   : ")
        jml_inp = input("Jumlah  : ")
        pj = input("PJ      : ")

        if jml_inp.isdigit():
            jumlah = int(jml_inp)
        else:
            jumlah = 0
            print("Jumlah bukan angka. Jumlah disimpan sebagai 0.")

        data_takjil[counter] = {
            "tanggal": tanggal,
            "waktu": waktu,
            "lokasi": lokasi,
            "jenis": jenis,
            "jumlah": jumlah,
            "pj": pj
        }

        print("Data No.", counter, "ditambahkan!")
        counter = counter + 1

    # READ
    elif pilihan == "2":
        print("\n-- DAFTAR DATA --")

        if len(data_takjil) == 0:
            print("Data kosong.")
        else:
            print("-" * 90)
            print(f"{'No':<4} {'Tanggal':<12} {'Waktu':<8} "
                  f"{'Lokasi':<18} {'Jenis':<15} {'Jumlah':<8} {'PJ'}")
            print("-" * 90)

            for no, d in data_takjil.items():
                print(f"{no:<4} {d['tanggal']:<12} "
                      f"{d['waktu']:<8} {d['lokasi']:<18} "
                      f"{d['jenis']:<15} {d['jumlah']:<8} {d['pj']}")

            print("-" * 90)
            print("Total:", len(data_takjil), "data")

    # UPDATE
    elif pilihan == "3":
        print("\n-- UBAH DATA --")

        if len(data_takjil) == 0:
            print("Data kosong.")
        else:
            print("\nDaftar:")

            for no, d in data_takjil.items():
                print(f"  [{no}] {d['tanggal']} | "
                      f"{d['lokasi']} | {d['jenis']}")

            inp = input("\nPilih nomor yang diubah: ")

            if inp.isdigit():
                no = int(inp)

                if no in data_takjil:
                    old = data_takjil[no]

                    print("\nData saat ini:")
                    print("  1. Tanggal :", old["tanggal"])
                    print("  2. Waktu   :", old["waktu"])
                    print("  3. Lokasi  :", old["lokasi"])
                    print("  4. Jenis   :", old["jenis"])
                    print("  5. Jumlah  :", old["jumlah"])
                    print("  6. PJ      :", old["pj"])

                    print("\nMasukkan nilai BARU "
                          "(tekan Enter jika tidak diubah):")

                    new_tgl = input(
                        "  Tanggal baru [" + old["tanggal"] + "]: ")
                    new_wkt = input(
                        "  Waktu baru   [" + old["waktu"] + "]: ")
                    new_lok = input(
                        "  Lokasi baru  [" + old["lokasi"] + "]: ")
                    new_jns = input(
                        "  Jenis baru   [" + old["jenis"] + "]: ")
                    new_jml = input(
                        "  Jumlah baru  [" + str(old["jumlah"]) + "]: ")
                    new_pj = input(
                        "  PJ baru      [" + old["pj"] + "]: ")

                    if new_tgl != "":
                        old["tanggal"] = new_tgl

                    if new_wkt != "":
                        old["waktu"] = new_wkt

                    if new_lok != "":
                        old["lokasi"] = new_lok

                    if new_jns != "":
                        old["jenis"] = new_jns

                    if new_jml != "":
                        if new_jml.isdigit():
                            old["jumlah"] = int(new_jml)
                        else:
                            print("Jumlah harus berupa angka. "
                                  "Jumlah lama tetap digunakan.")

                    if new_pj != "":
                        old["pj"] = new_pj

                    print("\nData berhasil diperbarui!")
                    print("Verifikasi:", data_takjil[no])

                else:
                    print("Nomor tidak valid.")
            else:
                print("Input harus angka.")

    # DELETE
    elif pilihan == "4":
        print("\n-- HAPUS DATA --")

        if len(data_takjil) == 0:
            print("Data kosong.")
        else:
            for no, d in data_takjil.items():
                print(f"  [{no}] {d['tanggal']} | "
                      f"{d['lokasi']} | {d['jenis']}")

            inp = input("\nPilih nomor yang dihapus: ")

            if inp.isdigit():
                no = int(inp)

                if no in data_takjil:
                    konfirmasi = input("Yakin hapus? (y): ")

                    if konfirmasi.lower() == "y":
                        del data_takjil[no]
                        print("Data terhapus.")
                    else:
                        print("Penghapusan dibatalkan.")
                else:
                    print("Nomor tidak valid.")
            else:
                print("Input harus angka.")

    # EXIT
    elif pilihan == "5":
        print("\nTerima kasih!")
        break

    else:
        print("Pilih 1-5.")

print("Program selesai.")