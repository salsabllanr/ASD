from prettytable import PrettyTable
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def merge_sort_linked_list(head, key=None):
    if not head or not head.next:
        return head

    mid = get_middle(head)
    mid_next = mid.next
    mid.next = None

    left = merge_sort_linked_list(head, key=key)
    right = merge_sort_linked_list(mid_next, key=key)

    return merge(left, right, key=key)

def merge(left, right, key=None):
    dummy = MahasiswaNode()
    current = dummy

    while left and right:
        if key:
            if key(left) < key(right):
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
        else:
            if left < right:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
        current = current.next

    if left:
        current.next = left
    else:
        current.next = right

    return dummy.next

def get_middle(head):
    if not head:
        return head

    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

class MahasiswaNode:
    def __init__(self, nim=None, nama=None, fakultas=None, jurusan=None, angkatan=None, kelas=None, next=None, prev=None):
        self.nim = nim
        self.nama = nama
        self.fakultas = fakultas
        self.jurusan = jurusan
        self.angkatan = angkatan
        self.kelas = kelas
        self.next = next
        self.prev = prev

    def __lt__(self, other):
        return self.nim < other.nim

    def __gt__(self, other):
        return self.nim > other.nim

    def __eq__(self, other):
        return self.nim == other.nim

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length

    def display(self):
        table = PrettyTable()
        table.field_names = ["NIM", "Nama", "Fakultas", "Jurusan", "Angkatan", "Kelas"]
        current = self.head
        while current:
            table.add_row([current.nim, current.nama, current.fakultas, current.jurusan, current.angkatan, current.kelas])
            current = current.next
        print(table)

    def search(self, nim):
        current = self.head
        while current:
            if current.nim == nim:
                return current
            current = current.next
        return None

    def delete(self, nim):
        node_to_delete = self.search(nim)
        if not node_to_delete:
            print("Data mahasiswa dengan NIM", nim, "tidak ditemukan.")
            return
        if node_to_delete.prev:
            node_to_delete.prev.next = node_to_delete.next
        else:
            self.head = node_to_delete.next
        if node_to_delete.next:
            node_to_delete.next.prev = node_to_delete.prev
        else:
            self.tail = node_to_delete.prev
        del node_to_delete

    def update(self, nim, node_baru):
        node_to_update = self.search(nim)
        if not node_to_update:
            print("Data mahasiswa dengan NIM", nim, "tidak ditemukan.")
            return
        if node_baru.nama:
            node_to_update.nama = node_baru.nama
        if node_baru.fakultas:
            node_to_update.fakultas = node_baru.fakultas
        if node_baru.jurusan:
            node_to_update.jurusan = node_baru.jurusan
        if node_baru.angkatan:
            node_to_update.angkatan = node_baru.angkatan
        if node_baru.kelas:
            node_to_update.kelas = node_baru.kelas

    def tambah_di_awal(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def tambah_di_akhir(self, node):      
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

    def tambah_setelah_nim(self, posisi, node):
        new_node = MahasiswaNode(node.nim, node.nama, node.fakultas, node.jurusan, node.angkatan, node.kelas)
        current = self.head
        while current:
            if current.nim == posisi:
                new_node.prev = current
                new_node.next = current.next
                if current.next:
                    current.next.prev = new_node
                else:
                    self.tail = new_node
                current.next = new_node
                break
            current = current.next

    def hapus_di_awal(self):
        if not self.head:
            print("Linked list kosong. Tidak ada yang dihapus.")
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def hapus_di_akhir(self):
        if not self.head:
            print("Linked list kosong. Tidak ada yang dihapus.")
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def hapus_berdasarkan_nim(self, nim):
        if not self.head:
            print("Linked list kosong. Tidak ada yang dihapus.")
            return
        current = self.head
        while current:
            if current.nim == nim:
                if current == self.head:
                    self.hapus_di_awal()
                elif current == self.tail:
                    self.hapus_di_akhir()
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                break
            current = current.next

    def jump_search(self, x):
        n = len(self)
        if n == 0:
            return None
        step = int(n ** 0.5)
        prev = 0
        while prev < n and self[prev].nim.lower() < x.lower():
            prev = min(prev + step, n - 1)
        while prev >= 0 and self[prev].nim.lower() > x.lower():
            prev -= 1
        if prev >= 0 and self[prev].nim.lower() == x.lower():
            return self[prev]
        return None

    def jump_search_by_name(self, x):
        n = len(self)
        if n == 0:
            return None
        step = int(n ** 0.5)
        prev = 0
        while prev < n and self[prev].nama.lower() < x.lower(): 
            prev = min(prev + step, n - 1)
        while prev >= 0 and self[prev].nama.lower() > x.lower(): 
            prev -= 1
        if prev >= 0 and self[prev].nama.lower() == x.lower():  
            return self[prev]
        return None

    def __getitem__(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                return current
            count += 1
            current = current.next
        raise IndexError("Index out of range")

def tampilanMenu():
    clear()
    print("✦========================== MENU PROGRAM ============================✦")
    print("| 1. Tampilkan Data Mahasiswa                                        |")
    print("| 2. Urutan NIM Mahasiswa                                            |")
    print("| 3. Urutan Nama Mahasiswa                                           |")
    print("| 4. Tambah Data Mahasiswa                                           |")
    print("| 5. Hapus Data Mahasiswa                                            |")
    print("| 6. Update Data Mahasiswa                                           |")
    print("| 7. Cari Data Mahasiswa Berdasarkan NIM                             |")
    print("| 8. Cari Data Mahasiswa Berdasarkan Nama                            |")
    print("| 9. Keluar                                                          |")
    print("✦====================================================================✦")

dataMahasiswa = DoubleLinkedList()
mahasiswa1 = MahasiswaNode("210911", "Salsabilla", "Ilmu Komputer", "Teknik Informatika", "2021", "A")
mahasiswa2 = MahasiswaNode("220910", "Bagaskara", "Pendidikan Dokter", "Kedokteran", "2022", "C")
mahasiswa3 = MahasiswaNode("230912", "Zvylen", "Bisnis", "Ekonomi Bisnis", "2023", "B")
mahasiswa4 = MahasiswaNode("230809", "Gara", "Hukum", "Hukum", "2023", "B1")
mahasiswa5 = MahasiswaNode("211114", "Malio", "Musik", "Ilmu Sosial dan Budaya", "2021", "A1")
dataMahasiswa.tambah_di_akhir(mahasiswa1)
dataMahasiswa.tambah_di_akhir(mahasiswa2)
dataMahasiswa.tambah_di_akhir(mahasiswa3)
dataMahasiswa.tambah_di_akhir(mahasiswa4)
dataMahasiswa.tambah_di_akhir(mahasiswa5)

while True:
    tampilanMenu()
    try:
        pilihMenu = int(input("Pilih menu: "))
        if pilihMenu == 1:
            dataMahasiswa.display()
            input("(Enter untuk lanjutkan)")

        elif pilihMenu == 2:
            sorted_dataMahasiswa = DoubleLinkedList()
            current = dataMahasiswa.head
            while current:
                sorted_dataMahasiswa.tambah_di_akhir(MahasiswaNode(current.nim, current.nama, current.fakultas, current.jurusan, current.angkatan, current.kelas))
                current = current.next
            dataMahasiswa.head = merge_sort_linked_list(sorted_dataMahasiswa.head)
            dataMahasiswa.display()
            input("(Enter untuk lanjutkan)")

        elif pilihMenu == 3:
            sorted_dataMahasiswa = DoubleLinkedList()
            current = dataMahasiswa.head
            while current:
                sorted_dataMahasiswa.tambah_di_akhir(MahasiswaNode(current.nim, current.nama, current.fakultas, current.jurusan, current.angkatan, current.kelas))
                current = current.next
            dataMahasiswa.head = merge_sort_linked_list(sorted_dataMahasiswa.head, key=lambda x: x.nama.lower())
            dataMahasiswa.display()
            input("(Enter untuk lanjutkan)")

        elif pilihMenu == 4:
            nim = input("Masukan NIM : ")
            nama = input("Masukan Nama : ")
            fakultas = input("Masukan Nama Fakultas : ")
            jurusan = input("Masukan Nama Jurusan : ")
            angkatan = input("Masukan Angkatann: ")
            kelas = input("Masukan Kelas : ")
            data = MahasiswaNode(nim, nama, fakultas, jurusan, angkatan, kelas)
            print("1. Tambah di Awal")
            print("2. Tambah di Akhir")
            print("3. Tambah Setelah NIM Tertentu")
            pilihan = int(input("Pilih metode penambahan: "))
            if pilihan == 1:
                dataMahasiswa.tambah_di_awal(data)
            elif pilihan == 2:
                dataMahasiswa.tambah_di_akhir(data)
            elif pilihan == 3:
                dataMahasiswa.display()
                posisi = input("Masukkan NIM setelah posisi: ")
                dataMahasiswa.tambah_setelah_nim(posisi, data)
            print("\nData mahasiswa berhasil ditambahkan!")
            input("(Enter untuk lanjutkan)")

        elif pilihMenu == 5:
            print("1. Hapus di Awal")
            print("2. Hapus di Akhir")
            print("3. Hapus Berdasarkan NIM")
            pilihan_hapus = int(input("Pilih metode penghapusan: "))
            if pilihan_hapus == 1:
                dataMahasiswa.hapus_di_awal()
            elif pilihan_hapus == 2:
                dataMahasiswa.hapus_di_akhir()
            elif pilihan_hapus == 3:
                nim = input("Masukkan NIM mahasiswa yang ingin dihapus: ")
                dataMahasiswa.hapus_berdasarkan_nim(nim)
            input("(Enter untuk lanjutkan)")

        elif pilihMenu == 6:
            dataMahasiswa.display()
            nim = input("Masukan NIM mahasiswa yang ingin diupdate: ")
            nama = input("Masukan Nama baru: ")
            fakultas = input("Masukan Nama Fakultas baru: ")
            jurusan = input("Masukan Nama Jurusan baru: ")
            angkatan = input("Masukan Angkatan baru: ")
            kelas = input("Masukan Kelas baru: ")
            mahasiswa_baru = MahasiswaNode(nim, nama, fakultas, jurusan, angkatan, kelas)
            dataMahasiswa.update(nim, mahasiswa_baru)
            print("Data mahasiswa dengan NIM {} berhasil diupdate.".format(nim))
            input("(Enter untuk lanjutkan)")

        elif pilihMenu == 7:
            sorted_dataMahasiswa = DoubleLinkedList()
            current = dataMahasiswa.head
            while current:
                sorted_dataMahasiswa.tambah_di_akhir(MahasiswaNode(current.nim, current.nama, current.fakultas, current.jurusan, current.angkatan, current.kelas))
                current = current.next
            sorted_dataMahasiswa.head = merge_sort_linked_list(sorted_dataMahasiswa.head, key=lambda x: x.nim)
            nim = input("Masukkan NIM mahasiswa yang ingin dicari: ")
            result = dataMahasiswa.jump_search(nim)
            if result:
                print("Data mahasiswa dengan NIM {} ditemukan:".format(nim))
                print("Nama:", result.nama)
                print("Fakultas:", result.fakultas)
                print("Jurusan:", result.jurusan)
                print("Angkatan:", result.angkatan)
                print("Kelas:", result.kelas)
            else:
                print("Data mahasiswa dengan NIM", nim, "tidak ditemukan.")
            input("(Enter untuk melanjutkan)")

        elif pilihMenu == 8:
            sorted_dataMahasiswa = DoubleLinkedList()
            current = dataMahasiswa.head
            while current:
                sorted_dataMahasiswa.tambah_di_akhir(MahasiswaNode(current.nim, current.nama, current.fakultas, current.jurusan, current.angkatan, current.kelas))
                current = current.next
            sorted_dataMahasiswa.head = merge_sort_linked_list(sorted_dataMahasiswa.head, key=lambda x: x.nama.lower())
            nama = input("Masukkan Nama mahasiswa yang ingin dicari: ")
            result = sorted_dataMahasiswa.jump_search_by_name(nama)
            if result:
                print("Data mahasiswa dengan Nama {} ditemukan:".format(nama))
                print("NIM:", result.nim)
                print("Fakultas:", result.fakultas)
                print("Jurusan:", result.jurusan)
                print("Angkatan:", result.angkatan)
                print("Kelas:", result.kelas)
            else:
                print("Data mahasiswa dengan Nama", nama, "tidak ditemukan.")
            input("(Enter untuk melanjutkan)")

        elif pilihMenu == 9:
            clear()
            print("✦======================================================================✦")
            print("|                        PROGRAM TELAH SELESAI                         |")
            print("✦======================================================================✦")
            print("|           TERIMAKASIH TELAH MENGGUNAKAN PROGRAM SEDERHANA            |")
            print("|              YANG DISUSUN OLEH ADINDA SALSABILLA NAURA               |")
            print("|                         SISTEM INFORMASI A'23                        |")
            print("|                                  |||                                 |")
            print("|                         UNIVERSITAS MULAWARMAN                       |")
            print("✦======================================================================✦")
            break
        else:
            print("Masukkan angka antara 1 sampai 9.")
            input("Enter untuk melanjutkan...")
    except ValueError:
        print("\nMasukkan angka antara 1 sampai 9")
        input("Enter untuk melanjutkan...")