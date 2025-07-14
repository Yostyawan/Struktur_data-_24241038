# Minta input data customer
nama = input("Masukkan nama customer: ")
tanggal_belanja = input("Masukkan tanggal belanja (YYYY-MM-DD): ")

# Simpan data customer ke tuple
data_customer = (nama, tanggal_belanja)

# Minta jumlah barang
jumlah_barang = int(input("Masukkan jumlah barang: "))

# List untuk menampung dictionary barang
daftar_belanja = []  # Ini array/list of dict

for i in range(jumlah_barang):
    print(f"\nBarang ke-{i+1}")
    barang_nama = input("Nama barang: ")
    harga_satuan = int(input("Harga satuan: "))
    qty = int(input("Jumlah (qty): "))
    
    # Simpan data barang ke dictionary
    barang = {
        "nama": barang_nama,
        "harga_satuan": harga_satuan,
        "qty": qty,
        "subtotal": harga_satuan * qty
    }
    
    # Tambahkan dictionary barang ke list array
    daftar_belanja.append(barang)

# Hitung total belanja
total_belanja = sum(item["subtotal"] for item in daftar_belanja)

# Cetak output
print("\nData customer :")
print(f"Nama : {data_customer[0]}")
print(f"Tanggal belanja : {data_customer[1]}")
print("Daftar belanja :")

for idx, item in enumerate(daftar_belanja, start=1):
    print(f"{idx}. {item['nama']} - harga satuan : {item['harga_satuan']}, qty {item['qty']}")
from datetime import datetime

def catat_belanja_customer():
    # Input nama customer & tanggal belanja
    nama_customer = input("Masukkan nama customer: ")
    
    # Validasi format tanggal
    while True:
        tanggal_belanja = input("Masukkan tanggal belanja (YYYY-MM-DD): ")
        try:
            datetime.strptime(tanggal_belanja, "%Y-%m-%d")
            break
        except ValueError:
            print("Format tanggal salah! Gunakan format YYYY-MM-DD.")

    # Simpan dalam tuple
    data_customer = (nama_customer, tanggal_belanja)

    # Input jumlah barang, validasi harus bilangan bulat positif
    while True:
        try:
            jumlah_barang = int(input("Masukkan jumlah barang yang dibeli: "))
            if jumlah_barang <= 0:
                raise ValueError
            break
        except ValueError:
            print("Jumlah barang harus berupa bilangan bulat positif!")

    # List untuk menyimpan data barang
    daftar_barang = []

    for i in range(jumlah_barang):
        print(f"\nData barang ke-{i+1}:")

        nama_barang = input("Nama barang: ")

        # Validasi harga harus positif dan angka
        while True:
            try:
                harga = float(input("Harga barang: "))
                if harga < 0:
                    raise ValueError
                break
            except ValueError:
                print("Harga harus berupa angka positif!")

        # Validasi jumlah beli harus bilangan bulat positif
        while True:
            try:
                jumlah_beli = int(input("Jumlah beli: "))
                if jumlah_beli <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Jumlah beli harus berupa bilangan bulat positif!")

        barang = {
            "Nama Barang": nama_barang,
            "Harga": harga,
            "Jumlah Beli": jumlah_beli,
            "Total Harga": harga * jumlah_beli
        }

        daftar_barang.append(barang)

    # Tampilkan hasil
    print("\n===== RINCIAN BELANJA =====")
    print(f"Nama Customer : {data_customer[0]}")
    print(f"Tanggal Belanja : {data_customer[1]}")
    print("\nDaftar Barang:")

    total_belanja = 0
    total_item = 0

    for idx, barang in enumerate(daftar_barang, start=1):
        print(f"{idx}. {barang['Nama Barang']} - Jumlah: {barang['Jumlah Beli']} - Harga: Rp {barang['Harga']:.2f} - Total: Rp {barang['Total Harga']:.2f}")
        total_belanja += barang['Total Harga']
        total_item += barang['Jumlah Beli']

    print(f"\nTotal Item Dibeli: {total_item}")
    print(f"Total Belanja: Rp {total_belanja:.2f}")

    return data_customer, daftar_barang

if __name__ == "_main_":
    catat_belanja_customer()
print(f"Total belanja : Rp {total_belanja:,}".replace(",", "."))
