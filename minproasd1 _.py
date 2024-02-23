from prettytable import PrettyTable
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

class mahasiswa:
    def __init__(self, nim, nama, fakultas, jurusan, angkatan, kelas):
        self.nim = nim
        self.nama = nama
        self.fakultas = fakultas
        self.jurusan = jurusan
        self.angkatan = angkatan
        self.kelas = kelas

class crudMahasiswa :
    def __init__(self):
        self.dataMahasiswa = {}
    def tampilan(self) :
        if self.dataMahasiswa:
            table = PrettyTable()
            table.field_names = ["NIM", "Nama", "Fakultas", "Jurusan", "Angkatan", "Kelas"]
            for nim, mahasiswa in self.dataMahasiswa.items():
                table.add_row([mahasiswa.nim, mahasiswa.nama, mahasiswa.fakultas, mahasiswa.jurusan, mahasiswa.angkatan, mahasiswa.kelas])
            print(table)
        else:
            print("\nData Mahasiswa Belum Terdaftar")
    def cari(self, nim):
        if nim in self.dataMahasiswa:
            mahasiswa = self.dataMahasiswa[nim]
            print("Data Mahasiswa dengan NIM {} ditemukan:".format(nim))
            print("NIM:", mahasiswa.nim)
            print("Nama:", mahasiswa.nama)
            print("Fakultas:", mahasiswa.fakultas)
            print("Jurusan:", mahasiswa.jurusan)
            print("Angkatan:", mahasiswa.angkatan)
            print("Kelas:", mahasiswa.kelas)
        else:
            print("Data mahasiswa dengan NIM {} tidak ditemukan.".format(nim))

    def tambah(self, mahasiswa):
        self.dataMahasiswa[mahasiswa.nim] = mahasiswa

    def hapus(self, nim):
        if nim in self.dataMahasiswa:
            del self.dataMahasiswa[nim]
            print("Data mahasiswa dengan NIM {} berhasil dihapus.".format(nim))
            print("(Enter untuk lanjutkan)")
            a = input("")
        else:
            print("Data mahasiswa dengan NIM {} tidak ditemukan.".format(nim))

    def update(self, nim, mahasiswa_baru):
        if nim in self.dataMahasiswa:
            self.dataMahasiswa[nim] = mahasiswa_baru
            print("Data mahasiswa dengan NIM {} berhasil diupdate.".format(nim))
            print("(Enter untuk lanjutkan)")
            a = input("")
        else:
            print("Data mahasiswa dengan NIM {} tidak ditemukan.".format(nim))

def tampilanMenu():
    clear()
    print("+====================================================================+")
    print("|                           SELAMAT DATANG                           |")
    print("|                           Di SISFOR.FLIX                           |")
    print("+====================================================================+")
    print("|                        Silahkan Pilih Menu                         |")
    print("+====================================================================+")
    print("| [1]. Tampilkan Data                                                |")
    print("| [2]. Tambah Data                                                   |")
    print("| [3]. Hapus Data                                                    |")
    print("| [4]. Update Data                                                   |")
    print("| [5]. Keluar                                                        |")
    print("+====================================================================+")

dataMahasiswa = crudMahasiswa()
mahasiswa1 = mahasiswa("2009116023", "Lee Jeno", "Ilmu Komputer", "Teknik Informatika", "2020", "A")
mahasiswa2 = mahasiswa("2102166059", "Lee Heeseung", "Kedokteran", "Pendidikan Dokter", "2021", "B")
dataMahasiswa.tambah(mahasiswa1)
dataMahasiswa.tambah(mahasiswa2)
while True:
    tampilanMenu()
    try :
        pilihMenu = int(input("Pilih menu: "))
        if pilihMenu == 1:
            dataMahasiswa.tampilan()
            print("(Enter untuk lanjutkan)")
            a = input("")
        elif pilihMenu == 2:
            nim = input("Masukan NIM : ")
            nama = input("Masukan Nama : ")
            fakultas = input("Masukan Nama Fakultas : ")
            jurusan = input("Masukan Nama Jurusan : ")
            angkatan = input("Masukan Angkatann: ")
            kelas = input("Masukan Kelas : ")
            data = mahasiswa(nim, nama, fakultas, jurusan, angkatan, kelas)
            dataMahasiswa.tambah(data)
            print("\nData mahasiswa berhasil ditambahkan!")
            print("(Enter untuk lanjutkan)")
            a = input("")
            clear()
        elif pilihMenu == 3:
            dataMahasiswa.tampilan()
            nim = input("Masukan NIM mahasiswa yang ingin dihapus: ")
            dataMahasiswa.hapus(nim)
            print("Data mahasiswa dengan NIM {} berhasil dihapus.".format(nim))
        elif pilihMenu == 4:
            dataMahasiswa.tampilan()
            nim = input("Masukan NIM mahasiswa yang ingin diupdate: ")
            nama = input("Masukkan Nama Baru: ")
            fakultas = input("Masukkan Fakultas Baru: ")
            jurusan = input("Masukkan Jurusan Baru: ")
            angkatan = input("Masukkan Angkatan Baru: ")
            kelas = input("Masukkan Kelas Baru: ")
            mahasiswa_baru = mahasiswa(nim, nama, fakultas, jurusan, angkatan, kelas)
            dataMahasiswa.update(nim, mahasiswa_baru)
            dataMahasiswa.tampilan()
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