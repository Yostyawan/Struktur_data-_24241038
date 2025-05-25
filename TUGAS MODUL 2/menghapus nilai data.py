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

    # Menghapus node pertama (awal)
    def hapus_awal(self):
        if self.head is None:
            print("List kosong, tidak ada yang dihapus.")
            return
        # Jika list hanya memiliki satu node
        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

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

print("Sebelum dihapus node awal:")
dll.tampilkan()

dll.hapus_awal()

print("Setelah dihapus node awal:")
dll.tampilkan()