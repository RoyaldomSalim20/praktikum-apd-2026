#batas = 5
#for i in range(batas):
#    print("Perulangan ke-", i)

#for sapa in range(5):
#    print("Halo, selamat siang!")

#praktikum = ["apd", "orsikom", "jarkom", 70, 89, 77]
#for i in praktikum:
#    print(i)
#    print(i, end=" ")

#for i in range(1,10,2):
#    print("angka ke-i adalah", i)

#for i in range(1, 3):
#    for j in range(1, 4):
#        print(f'{i} x {j} = {i * j}')
#print('')

#jawab = "ya"
#hitung = 0

#while(jawab == "ya"):
#    hitung += 1
#    jawab = input("Ulang lagi tidak? ")
#print(f"Total Perulangan : {hitung}")

#username = "Afuza"
#batas = 0
#while batas < 3:
#    login = input("Masukkan username: ")
#    if login != username:
#        batas += 1
#    else:
#        batas = 3

#for i in range(10):
#    print(i)
#    if i == 5:
#        break

#for i in range(10):
#    if i % 2 == 0:
#        continue
#    print(i)

#for i in range(1, 4):
#    if i == 2:
#        break
#    print(i)

#tinggi = int(input("masukkan tinggi diinginkan: "))
#for i in range(1, tinggi + 1):
#    print("*" * (i))

tinggi = int(input("Masukkan tinggi diinginkan: "))
for i in range(tinggi):
   print (" " * (tinggi - i - 1), end="")
   print ("*" * (i+1))