class Node:
    def __init__(self, data):
        self.data = data        # Data yang disimpan
        self.prev = None        # Referensi ke node sebelumnya
        self.next = None        # Referensi ke node berikutnya

class DoubleLinkedList:
    def __init__(self):
        self.head = None        # Awal list

    # Menambah data di akhir list
    def tambah_akhir(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            # Cari node terakhir
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

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
dll.tambah_akhir(1)
dll.tambah_akhir(2)
dll.tambah_akhir(3)

dll.tampilkan()  # Output: Isi list: 1 <-> 2 <-> 3