from prettytable import PrettyTable
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

class MahasiswaNode:
    def __init__(self, nim, nama, fakultas, jurusan, angkatan, kelas):
        self.nim = nim
        self.nama = nama
        self.fakultas = fakultas
        self.jurusan = jurusan
        self.angkatan = angkatan
        self.kelas = kelas
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

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

def tampilanMenu():
    clear()
    print("✦========================== MENU PROGRAM ============================✦")
    print("| 1. Tampilkan Data Mahasiswa                                        |")
    print("| 2. Tambah Data Mahasiswa                                           |")
    print("| 3. Hapus Data Mahasiswa                                            |")
    print("| 4. Update Data Mahasiswa                                           |")
    print("| 5. Keluar                                                          |")
    print("✦=====================================================================✦")

dataMahasiswa = DoubleLinkedList()
mahasiswa1 = MahasiswaNode("2109116059", "Adinda Salsabilla Naura", "Ilmu Komputer", "Teknik Informatika", "2021", "A")
dataMahasiswa.tambah_di_akhir(mahasiswa1)
while True:
    tampilanMenu()
    try :
        pilihMenu = int(input("Pilih menu: "))
        if pilihMenu == 1:
            dataMahasiswa.display()
            print("(Enter untuk lanjutkan)")
            a = input("")
        elif pilihMenu == 2:
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
            print("(Enter untuk lanjutkan)")
            a = input("")
            clear()
        elif pilihMenu == 3:
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
            print("(Enter untuk lanjutkan)")
            a = input("")
        elif pilihMenu == 4:
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
        elif pilihMenu == 5:
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
            print("Masukkan angka antara 1 sampai 5.")
            input("Enter untuk melanjutkan...")
    except ValueError:
        print("\nMasukkan angka antara 1 sampai 5")
        input("Enter untuk melanjutkan...")