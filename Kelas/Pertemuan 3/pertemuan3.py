#praktikum = "Orsikom"

#if praktikum == "APD":
#    print("kamu lagi mengikuti praktikum APD sekarang!")
#else:
#    print("kamu lagi mengikuti praktikum lain!")

#Umur = int(input("Masukkan umur anda: "))

#if Umur < 17:
#    print("Anda belum cukup umur untuk mengikuti praktikum ini.")
#else:
#    print("Anda cukup umur untuk mengikuti praktikum ini!")

#kendaraan = input("Masukkan jenis kendaraan (mobil/motor/lainnya): ").lower()

#if kendaraan == "mobil":
#    tarif_parkir = 10000
#elif kendaraan == "motor":
#    tarif_parkir = 5000
#else:
#    tarif_parkir = 15000

#print("Tarif parkir yang harus dibayar:", tarif_parkir)

#Umur = "20"
#status = "Dewasa" if Umur == "20" else "Belum Dewasa"
#print(status)

#Umur = 16
#status = "Boleh masuk acara" if Umur >= 16 else "belum boleh masuk acara"
#print(status)

total = int(input("Masukkan total belanja: "))

if total >= 100000:
    print("Selamat! Anda mendapatkan diskon 10%")
elif total >= 200000:
    print("Selamat! Anda mendapatkan diskon 30%")
else:
    print("Maaf, anda tidak mendapatkan diskon.")