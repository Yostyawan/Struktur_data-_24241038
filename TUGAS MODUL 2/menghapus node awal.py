class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    # Menambah data di akhir list
    def tambah_akhir(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    # Menghapus node berdasarkan nilai data tertentu
    def hapus_data(self, data):
        current = self.head
        while current:
            if current.data == data:
                # Jika node yang akan dihapus adalah head
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                else:
                    # Jika node berada di tengah atau akhir
                    if current.next:
                        current.prev.next = current.next
                        current.next.prev = current.prev
                    else:
                        # Jika node adalah node terakhir
                        current.prev.next = None
                print(f"Node dengan data {data} telah dihapus.")
                return
            current = current.next
        print(f"Node dengan data {data} tidak ditemukan.")

    # Menampilkan semua data dari depan ke belakang
    def tampilkan(self):
        current = self.head
        print("Isi list: ", end='')
        while current:
            print(current.data, end=' <-> ' if current.next else '')
            current = current.next
        print()

# Contoh penggunaan
dll = DoubleLinkedList()
dll.tambah_akhir(10)
dll.tambah_akhir(20)
dll.tambah_akhir(30)
dll.tambah_akhir(20)
dll.tambah_akhir(40)

print("Sebelum dihapus data 20:")
dll.tampilkan()

dll.hapus_data(20)

print("Setelah dihapus data 20:")
dll.tampilkan()

dll.hapus_data(100)  # mencoba hapus data yang tidak ada