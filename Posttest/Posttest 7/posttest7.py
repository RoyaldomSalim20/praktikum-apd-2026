nama_program = "PROGRAM PEMBAGIAN TAKJIL"
data_takjil = {}
counter = 1

def hitung_total_data():
    """Mengembalikan jumlah data yang tersimpan."""
    return len(data_takjil)


def hitung_total_jumlah():
    """Mengembalikan total jumlah atau porsi takjil."""
    total = 0

    for data in data_takjil.values():
        total += data["jumlah"]

    return total

def perbarui_data(nomor, perubahan):
    """Memperbarui data berdasarkan nomor dan perubahan."""

    if nomor not in data_takjil:
        return False

    kolom_valid = (
        "tanggal", "waktu", "lokasi",
        "jenis", "jumlah", "pj"
    )

    for kolom, nilai in perubahan.items():
        if kolom in kolom_valid:
            data_takjil[nomor][kolom] = nilai

    return True

def hapus_data(nomor):
    """Menghapus data berdasarkan nomor."""

    if nomor in data_takjil:
        del data_takjil[nomor]
        return True

    return False

def tambah_data():
    global counter

    print("\n-- TAMBAH DATA BARU --")

    tanggal = input("Tanggal : ").strip()
    waktu = input("Waktu   : ").strip()
    lokasi = input("Lokasi  : ").strip()
    jenis = input("Jenis   : ").strip()
    pj = input("PJ      : ").strip()

    while True:
        try:
            jumlah = int(input("Jumlah  : "))

            if jumlah < 0:
                raise ValueError(
                    "Jumlah tidak boleh negatif."
                )

        except ValueError as error:
            print("Input jumlah tidak valid:", error)
            print("Masukkan bilangan bulat 0 atau lebih.")

        else:
            print("Jumlah berhasil divalidasi.")
            break

    data_takjil[counter] = {
        "tanggal": tanggal,
        "waktu": waktu,
        "lokasi": lokasi,
        "jenis": jenis,
        "jumlah": jumlah,
        "pj": pj
    }

    print("Data No.", counter, "berhasil ditambahkan!")
    counter += 1

def tampilkan_data():
    print("\n-- DAFTAR DATA TAKJIL --")

    if hitung_total_data() == 0:
        print("Data kosong.")

    else:
        print("-" * 100)

        print(
            f"{'No':<4} {'Tanggal':<14} {'Waktu':<10} "
            f"{'Lokasi':<20} {'Jenis':<18} "
            f"{'Jumlah':<10} {'PJ'}"
        )

        print("-" * 100)

        for nomor, data in data_takjil.items():
            print(
                f"{nomor:<4} {data['tanggal']:<14} "
                f"{data['waktu']:<10} "
                f"{data['lokasi']:<20} "
                f"{data['jenis']:<18} "
                f"{data['jumlah']:<10} {data['pj']}"
            )

        print("-" * 100)
        print("Total data         :", hitung_total_data())
        print("Total takjil/porsi :", hitung_total_jumlah())

print("=" * 55)
print("     " + nama_program)
print("=" * 55)

while True:
    print("\n" + "-" * 55)
    print(
        "MENU: 1.Tambahkan  2.Membaca  "
        "3.Perbarui  4.Hapus  5.Keluar"
    )
    print("-" * 55)

    try:
        pilihan = int(input("Pilih menu: "))

    except ValueError:
        print(
            "Input tidak valid. "
            "Menu harus berupa angka 1 sampai 5."
        )
        continue

    finally:
        print("Pemeriksaan input menu selesai.")

    if pilihan == 1:
        tambah_data()

    elif pilihan == 2:
        tampilkan_data()

    elif pilihan == 3:
        print("\n-- PERBARUI DATA --")

        if hitung_total_data() == 0:
            print("Data kosong. Tambahkan data terlebih dahulu.")
            continue

        tampilkan_data()

        try:
            nomor = int(
                input("Masukkan nomor data yang diubah: ")
            )

        except ValueError:
            print("Nomor harus berupa angka bulat.")
            continue

        if nomor not in data_takjil:
            print("Nomor data tidak ditemukan.")
            continue

        data_lama = data_takjil[nomor]
        perubahan = {}

        daftar_kolom = [
            ("tanggal", "Tanggal"),
            ("waktu", "Waktu"),
            ("lokasi", "Lokasi"),
            ("jenis", "Jenis"),
            ("jumlah", "Jumlah"),
            ("pj", "PJ")
        ]

        print("Tekan Enter jika nilai tidak ingin diubah.")

        for kolom, label in daftar_kolom:
            nilai_baru = input(
                f"{label} baru [{data_lama[kolom]}]: "
            ).strip()

            if nilai_baru == "":
                continue

            if kolom == "jumlah":
                try:
                    jumlah_baru = int(nilai_baru)

                    if jumlah_baru < 0:
                        raise ValueError(
                            "Jumlah tidak boleh negatif."
                        )

                except ValueError as error:
                    print("Jumlah tidak diubah:", error)
                    continue

                perubahan[kolom] = jumlah_baru

            else:
                perubahan[kolom] = nilai_baru

        if perubahan:
            if perbarui_data(nomor, perubahan):
                print("Data berhasil diperbarui.")
                print("Data terbaru:", data_takjil[nomor])
            else:
                print("Data gagal diperbarui.")

        else:
            print("Tidak ada perubahan yang dilakukan.")

    elif pilihan == 4:
        print("\n-- HAPUS DATA --")

        if hitung_total_data() == 0:
            print("Data kosong. Tidak ada data yang dapat dihapus.")
            continue

        tampilkan_data()

        try:
            nomor = int(
                input("Masukkan nomor data yang dihapus: ")
            )

        except ValueError:
            print("Nomor harus berupa angka bulat.")
            continue

        if nomor not in data_takjil:
            print("Nomor data tidak ditemukan.")
            continue

        konfirmasi = input(
            "Yakin menghapus data ini? (y/n): "
        ).strip().lower()

        if konfirmasi == "y":
            if hapus_data(nomor):
                print("Data berhasil dihapus.")
            else:
                print("Data gagal dihapus.")

        else:
            print("Penghapusan dibatalkan.")

    elif pilihan == 5:
        print("\nTerima kasih telah menggunakan program ini!")
        break

    else:
        print(
            "Pilihan tidak tersedia. "
            "Silakan pilih menu 1 sampai 5."
        )

print("Program selesai.")