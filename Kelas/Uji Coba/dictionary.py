mahasiswa = {
    "Nama"      : "Rafi",
    "NIM"       : "072",
    "Prodi"     : "Informatika",
    "Semester"  : "2"
}
mahasiswa["Alamat"] = "Jalan Sentosa"
mahasiswa["Email"] = "salimkhaerul20@gmail.com"
mahasiswa.update({"Semester": 3})

print(len(mahasiswa))

for i, j in mahasiswa.items():
    print(f"{i} : {j}")