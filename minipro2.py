import os
from prettytable import PrettyTable

class Instrumen:
    def __init__(self, nama, merek, kategori, harga, stok):
        self.nama = nama
        self.merek = merek
        self.kategori = kategori
        self.harga = harga
        self.stok = stok
        self.next_instrumen = None 

    def display_info(self):
        print(f"{self.nama} ({self.merek}) ({self.kategori}) - Rp.{self.harga}, stok: {self.stok}")

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def add_instrumen(self, instrumen):
        instrumen.next_instrumen = self.head
        self.head = instrumen

    def display_inventory(self):
        current = self.head
        print(f"\nInventory:")
        while current:
            current.display_info()
            current = current.next_instrumen

    def cari_instrumen(self, instrumen_nama):
        current = self.head
        while current:
            if current.nama.lower() == instrumen_nama.lower():
                return current
            current = current.next_instrumen
        return None

    def tambah_instrumen(self, nama, merek, kategori, harga, stok, print_message=True):
        new_instrumen = Instrumen(nama, merek, kategori, harga, stok)
        self.add_instrumen(new_instrumen)
        if print_message:
            print(f"\nInstrument '{nama}' telah ditambahkan!.")

    def update_instrumen(self, instrumen_nama, new_harga, new_stok):
        instrumen = self.cari_instrumen(instrumen_nama)
        if instrumen:
            instrumen.harga = new_harga
            instrumen.stok = new_stok
            print(f"\nInstrument '{instrumen_nama}' telah diupdate.")
        else:
            print(f"\nInstrument '{instrumen_nama}' tidak ditemukan.")

    def hapus_instrumen(self, instrumen_nama):
        current = self.head
        previous = None

        while current and current.nama.lower() != instrumen_nama.lower():
            previous = current
            current = current.next_instrumen

        if current:
            if previous:
                previous.next_instrumen = current.next_instrumen
            else:
                self.head = current.next_instrumen
            print(f"\nInstrument '{instrumen_nama}' telah dihapus.")
        else:
            print(f"\nInstrument '{instrumen_nama}' tidak ditemukan.")


class MusicShop:
    def __init__(self, nama, default_data=None):
        self.nama = nama
        self.inventory = DoubleLinkedList()

        if default_data:
            for data in default_data:
                self.inventory.tambah_instrumen(*data, print_message=False)

    def display_inventory(self):
            table = PrettyTable()  
            table.field_names = ["Nama", "Merek", "Kategori", "Harga", "Stok"] 

            current = self.inventory.head
            while current:
                table.add_row([current.nama, current.merek, current.kategori, f"Rp.{current.harga}", current.stok])
                current = current.next_instrumen

            print(table)

    def tambah_instrumen(self, nama, merek, kategori, harga, stok):
        self.inventory.tambah_instrumen(nama, merek, kategori, harga, stok)

    def update_instrumen(self, instrumen_nama, new_harga, new_stok):
        self.inventory.update_instrumen(instrumen_nama, new_harga, new_stok)

    def hapus_instrumen(self, instrumen_nama):
        self.inventory.hapus_instrumen(instrumen_nama)


def main():
    data_instrumen = [
        ("Guitar", "Fender", "String", 500000, 10),
        ("Keyboard", "Yamaha", "Piano", 800000, 5),
    ]

    music_shop = MusicShop("Melody Music", default_data=data_instrumen)

    while True:
        print("\nMusic Shop Dugong")
        print("\nPilihan:")
        print("1. Lihat Penyimpanan")
        print("2. Tambah Instrumen")
        print("3. Update Instrumen")
        print("4. Hapus Instrumen")
        print("0. Exit")

        choice = input("\nMasukkan Pilihan: ")

        if choice == "1":
            os.system("cls")
            music_shop.display_inventory()
        elif choice == "2":
            os.system("cls")
            nama = input("Masukkan Nama Instrumen: ")
            merek = input("Masukkan Merek Instrumen: ")
            kategori = input("Masukkan Kategori Instrumen: ")
            harga = float(input("Masukkan Harga Instrumen: "))
            stok = int(input("Masukkan Stok Instrumen: "))
            os.system("cls")
            music_shop.tambah_instrumen(nama, merek, kategori, harga, stok)
        elif choice == "3":
            os.system("cls")
            instrumen_nama = input("Masukkan nama instrumen yang akan diupdate: ")
            new_harga = float(input("Masukkan harga baru: "))
            new_stok = int(input("Masukkan stok baru: "))
            os.system("cls")
            music_shop.update_instrumen(instrumen_nama, new_harga, new_stok)
        elif choice == "4":
            os.system("cls")
            instrumen_nama = input("Masukkan nama instrumen yang akan dihapus: ")
            os.system("cls")
            music_shop.hapus_instrumen(instrumen_nama)
        elif choice == "0":
            os.system("cls")
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
