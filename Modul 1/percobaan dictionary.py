# membuat dictionary
data = {
    "nama"      : "Adam Bachtiar Maulachela",
    "NIDN"      : 62708078505,
    "Prodi"     : "Pendidikan Teknologi Informasi",
    "mat_kul"    : ['Algoritma dan Pemrograman', 'Struktur Data', 'PBO'],
    "status"    : True,
    "sosmed"    : {
        "Github"    : "@adamMaulachela",
        "twitter"   : '_',
        "instagram" : '-'
    }
}

# Cara kita mengakses dictionary dengan key
print("Nama Saya adalah %s" % data['nama'])
print("Akun Github saya %s" % data['sosmed']['Github'])

# cara lainnya dengan menggunakan .get
print("NIDN Saya adalah %s" % data.get('NIDN'))

# Mengubah nilai item dictionary dict dengan key
data['status'] = False

# Cek hasil perubahan
print(data['status'])

# Mengubah nilai item dictionary dengan .update
data.update({"sosmed" : {"twitter" : "@adammaulachaila"}})

# cek hasil perubahan
print(data['sosmed']['twitter'])

# Menghapus menggunakan perintah del
del data['status']

# cek hasil penghapusan data 
print(data)

# Menghapus item menggunkan method pop()
data.pop("sosmed")

# cek hasil penghapusan data 
print(data)

# menghapus data seluruhnya
data.clear()

# Menambah data dictionary
# membuat dictionary
mahasiswa = {
    "name" : "Adam Bachtiar Maulachela"
}

# menambahkan nim
mahasiswa.update({
    "nidn" : "0708078505"
})

# melihat hasilnya
print(mahasiswa)

# looping dictionary
# mencetak data pada dict secara berulang-ulang setiap key
for key in mahasiswa:
    print(key, mahasiswa[key])

# Atau:
for key, value in mahasiswa.items():
    print(f"{key}: {value}")