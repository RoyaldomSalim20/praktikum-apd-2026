#lemari = ["Baju", "Celana", 69, 7.2, True, 700, 222, 240]

#angka1 = [ [1, 2], [3, 4, 5] ]
#print(angka1[1][2])

#angka1 = [1, 3, 5]
#angka2 = [2, 4, 6]
#gabungan = angka1 + angka2
#print(gabungan)
#ulang = angka1 + angka2 * 3
#print(ulang)

#print("sebelum diubah:")
#print(lemari)
#lemari[0:2] = ["Celana Panjang", "Jaket", "Jas Hujan"]
#del lemari[1]
#lemari.remove("Celana")

#sisa = lemari.pop(2)

#print("setelah diubah:")
#print(lemari)

#for index, item in enumerate(lemari):
#    print(f"Index ke-{index + 1}: {item}")
#for item in lemari:
#     print(item)
#for item in lemari:
#    print(item)
#jumlah = 0
#for item in lemari:
#    if type(item) == int:
#        jumlah += 1
#        print(jumlah)

#angka = (1, 2, 3, "Halo", True)
#ubah= list(angka)
#ubah = ("hai")

#angka = tuple(ubah)
#print(angka)
#print(angka)

lemari = ("baju", "celana", "sepatu")
(atasan, *bawahan) = lemari
print(bawahan)