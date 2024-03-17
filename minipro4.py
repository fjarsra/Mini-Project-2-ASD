import os
from prettytable import PrettyTable

class Instrumen:
    id_counter = 1 

    def __init__(self, nama, merek, kategori, harga, stok):
        self.id = Instrumen.id_counter
        Instrumen.id_counter += 1

        self.nama = nama
        self.merek = merek
        self.kategori = kategori
        self.harga = harga
        self.stok = stok
        self.next_instrumen = None

    def display_info(self):
        print(f"ID: {self.id}, {self.nama} ({self.merek}) ({self.kategori}) - Rp.{self.harga:,.3f}, stok: {self.stok}")

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_instrumen(self, instrumen):
        if not self.head:
            self.head = instrumen
        else:
            self.tail.next_instrumen = instrumen
        self.tail = instrumen

    def display_inventory(self):
        table = PrettyTable()
        table.field_names = ["ID", "Nama", "Merek", "Kategori", "Harga", "Stok"]

        current = self.head
        while current:
            table.add_row([current.id, current.nama, current.merek, current.kategori, f"Rp.{current.harga:,.3f}", current.stok])
            current = current.next_instrumen
        print(table)

    def cari_instrumen(self, instrumen_id):
        current = self.head
        while current:
            if current.id == instrumen_id:
                return current
            current = current.next_instrumen
        return None

    def tambah_instrumen(self, nama, merek, kategori, harga, stok, print_message=True):
        new_instrumen = Instrumen(nama, merek, kategori, harga, stok)
        self.add_instrumen(new_instrumen)
        if print_message:
            print(f"\nInstrument '{nama}' dengan ID {new_instrumen.id} telah ditambahkan!.")

    def update_instrumen(self, instrumen_id, new_harga, new_stok):
        instrumen = self.cari_instrumen(instrumen_id)
        if instrumen:
            instrumen.harga = new_harga
            instrumen.stok = new_stok
            print(f"\nInstrument dengan ID {instrumen_id} telah diupdate.")
        else:
            print(f"\nInstrument dengan ID {instrumen_id} tidak ditemukan.")

    def hapus_instrumen(self, instrumen_id):
        current = self.head
        previous = None

        while current and current.id != instrumen_id:
            previous = current
            current = current.next_instrumen

        if current:
            if previous:
                previous.next_instrumen = current.next_instrumen
            if current == self.tail:  
                self.tail = previous
            else:
                self.head = current.next_instrumen
            if current == self.tail:  
                self.tail = None
            print(f"\nInstrument dengan ID {instrumen_id} telah dihapus.")
        else:
            print(f"\nInstrument dengan ID {instrumen_id} tidak ditemukan.")

    def quicksort(self, instrumens, key_func, reverse=False):
        if len(instrumens) <= 1:
            return instrumens
        pivot = instrumens[len(instrumens) // 2]
        left = [x for x in instrumens if key_func(x) < key_func(pivot)]
        middle = [x for x in instrumens if key_func(x) == key_func(pivot)]
        right = [x for x in instrumens if key_func(x) > key_func(pivot)]

        return self.quicksort(left, key_func, reverse) + middle + self.quicksort(right, key_func, reverse)

    def sort_by_harga(self, ascending=True):
        instrumens = self.get_instruments()
        sorted_list = self.quicksort(instrumens, key_func=lambda x: x.harga, reverse=not ascending)
        self.rebuild_list(sorted_list, reverse=not ascending)

    def sort_by_stok(self, ascending=True):
        instrumens = self.get_instruments()
        sorted_list = self.quicksort(instrumens, key_func=lambda x: x.stok, reverse=not ascending)
        self.rebuild_list(sorted_list, reverse=not ascending)

    def get_instruments(self):
        instruments = []
        current = self.head
        while current:
            instruments.append(current)
            current = current.next_instrumen
        return instruments

    def rebuild_list(self, sorted_list, reverse=False):
        if reverse:
            sorted_list = sorted_list[::-1]

        self.head = sorted_list[0]
        current = self.head
        for instrument in sorted_list[1:]:
            current.next_instrumen = instrument
            current = instrument
        self.tail = current
        current.next_instrumen = None

class MusicShop:
    def __init__(self, name, default_data=None):
        self.name = name
        self.inventory = DoubleLinkedList()

        if default_data:
            for data in default_data:
                self.inventory.tambah_instrumen(*data, print_message=False)

    def display_inventory(self):
        self.inventory.display_inventory()

    def tambah_instrumen(self, nama, merek, kategori, harga, stok):
        self.inventory.tambah_instrumen(nama, merek, kategori, harga, stok)

    def update_instrumen(self, instrumen_id, new_harga, new_stok):
        self.inventory.update_instrumen(instrumen_id, new_harga, new_stok)

    def hapus_instrumen(self, instrumen_id):
        self.inventory.hapus_instrumen(instrumen_id)

    def sort_inventory(self, sort_choice):
        if sort_choice == "1":
            self.inventory.sort_by_harga(ascending=True)
        elif sort_choice == "2":
            self.inventory.sort_by_harga(ascending=False)
        elif sort_choice == "3":
            self.inventory.sort_by_stok(ascending=True)
        elif sort_choice == "4":
            self.inventory.sort_by_stok(ascending=False)
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

    def find_instrument_by_id(self, instrument_id): 
        current = self.inventory.head
        while current:
            if current.id == instrument_id:
                return current
            current = current.next_instrumen
        return None 

    def search_instrument(self): 
        instrument_id = int(input("Masukkan ID instrumen untuk dicari: "))
        instrument = self.find_instrument_by_id(instrument_id)

        if instrument:
            print(f"\nInstrument ditemukan:")
            instrument.display_info() 
        else:
            print(f"Instrument dengan ID {instrument_id} tidak ditemukan.") 


def main():
    data_instrumen = [
        ("Guitar", "Fender", "String", 500000, 10),
        ("Keyboard", "Yamaha", "Piano", 800000, 5),
        ("Drums", "Pearl", "Percussion", 1200000, 3),
        ("Violin", "Stradivarius", "String", 1500000, 7),
        ("Trumpet", "Yamaha", "Brass", 700000, 8) 
    ]

    music_shop = MusicShop("Melody Music", default_data=data_instrumen)

    while True:
        print("\nMusic Shop Dugong")
        print("\nPilihan:")
        print("1. Lihat Penyimpanan")
        print("2. Tambah Instrumen")
        print("3. Update Instrumen")
        print("4. Hapus Instrumen")
        print("5. Sort Instrumen")
        print("6. Cari Instrumen")
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
            instrumen_id = int(input("Masukkan ID instrumen yang akan diupdate: "))
            new_harga = float(input("Masukkan harga baru: "))
            new_stok = int(input("Masukkan stok baru: "))
            os.system("cls")
            music_shop.update_instrumen(instrumen_id, new_harga, new_stok)
        elif choice == "4":
            os.system("cls")
            instrumen_id = int(input("Masukkan ID instrumen yang akan dihapus: "))
            os.system("cls")
            music_shop.hapus_instrumen(instrumen_id)
        elif choice == "5":
            os.system("cls")
            sort_choice = input("Pilih metode sorting:\n1. Sort by Harga (ascending)\n2. Sort by Harga (descending)\n3. Sort by Stok (ascending)\n4. Sort by Stok (descending)\nMasukkan Pilihan: ")
            music_shop.sort_inventory(sort_choice)
        elif choice == "6":
            os.system("cls")
            music_shop.search_instrument()
        elif choice == "0":
            os.system("cls")
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
