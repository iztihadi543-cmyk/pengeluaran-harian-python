# Modul untuk mengolah data pengeluaran

# Class untuk menyimpan satu transaksi
class Transaksi:
    def __init__(self, tanggal, kategori, keterangan, nominal):
        # Menyimpan data transaksi
        self.tanggal = tanggal
        self.kategori = kategori
        self.keterangan = keterangan
        self.nominal = nominal

    # Menampilkan transaksi dalam bentuk teks
    def tampilkan(self):
        return (
            f"{self.tanggal} | {self.kategori} | "
            f"{self.keterangan} | Rp{self.nominal}"
        )
# Class untuk mengelola kumpulan transaksi
class PengelolaPengeluaran:
    def __init__(self):
        # Menyiapkan daftar transaksi kosong
        self.transaksi = []
    # Menambahkan satu atau beberapa transaksi menggunakan *args
    def tambah_transaksi(self, *args):
        for transaksi in args:
            self.transaksi.append(transaksi)

    # Menampilkan daftar transaksi
    def tampilkan_semua(self):
        for transaksi in self.transaksi:
            print(transaksi.tampilkan())

    # Menghitung total pengeluaran
    def hitung_total(self):
        total = sum(
            transaksi.nominal for transaksi in self.transaksi
        )
        return total

    # Menghitung pengeluaran berdasarkan kategori
    def total_kategori(self, kategori):
        total = sum(
            transaksi.nominal
            for transaksi in self.transaksi
            if transaksi.kategori.lower() == kategori.lower()
        )
        return total

    # Membuat ringkasan menggunakan **kwargs
    def buat_ringkasan(self, **kwargs):
        total = self.hitung_total()

        # Mengambil nama pemilik jika diberikan
        pemilik = kwargs.get("pemilik", "Pengguna")

        return {
            "pemilik": pemilik,
            "jumlah_transaksi": len(self.transaksi),
            "total_pengeluaran": total
        }
    
# Fungsi untuk mengubah angka menjadi format rupiah
def format_rupiah(nominal):
    return f"Rp{nominal:,}".replace(",", ".")

# Pengujian lokal jika file dijalankan langsung
if __name__ == "__main__":
    # Membuat beberapa objek transaksi
    transaksi1 = Transaksi(
        "11-10-2026", "Makanan", "Makan siang", 15000
    )
    transaksi2 = Transaksi(
        "11-10-2026", "Transportasi", "Ongkos", 10000
    )

    # Membuat objek pengelola
    pengelola = PengelolaPengeluaran()

    # Memanggil fungsi dengan argumen kata kunci
    pengelola.tambah_transaksi(
        transaksi1,
        transaksi2
    )

    # Contoh penggunaan lambda untuk mengurutkan nominal
    urutkan = lambda transaksi: transaksi.nominal
    pengelola.transaksi.sort(key=urutkan)

    # Membuat ringkasan dengan keyword argument
    ringkasan = pengelola.buat_ringkasan(pemilik="Iztihadi")

    # Menampilkan hasil
    pengelola.tampilkan_semua()
    print("Total:", format_rupiah(ringkasan["total_pengeluaran"]))
    print("Pemilik:", ringkasan["pemilik"])