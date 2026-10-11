# Modul untuk mengolah data pengeluaran


# Class untuk menyimpan satu transaksi
class Transaksi:
    def __init__(self, tanggal, kategori, keterangan, nominal):
        # Menyimpan data transaksi
        self.tanggal = tanggal
        self.kategori = kategori
        self.keterangan = keterangan
        self.nominal = nominal

    # Mengubah data transaksi menjadi teks
    def tampilkan(self):
        return (
            f"{self.tanggal} | {self.kategori} | "
            f"{self.keterangan} | Rp{self.nominal}"
        )


# Class untuk mengelola transaksi
class PengelolaPengeluaran:
    def __init__(self):
        # Menyiapkan daftar transaksi
        self.transaksi = []

    # Menambahkan satu atau beberapa transaksi
    def tambah_transaksi(self, *args):
        for transaksi in args:
            self.transaksi.append(transaksi)

    # Menampilkan semua transaksi
    def tampilkan_semua(self):
        for transaksi in self.transaksi:
            print(transaksi.tampilkan())

    # Menghitung seluruh pengeluaran
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

    # Membuat ringkasan pengeluaran
    def buat_ringkasan(self, **kwargs):
        return {
            "pemilik": kwargs.get("pemilik", "Pengguna"),
            "jumlah_transaksi": len(self.transaksi),
            "total_pengeluaran": self.hitung_total()
        }

# Mengubah nominal menjadi format rupiah
def format_rupiah(nominal):
    return f"Rp{nominal:,}".replace(",", ".")

# Pengujian sederhana jika file dijalankan langsung
if __name__ == "__main__":
    transaksi1 = Transaksi(
        "11-10-2026", "Makanan", "Makan siang", 15000
    )

    transaksi2 = Transaksi(
        "11-10-2026", "Transportasi", "Ongkos", 10000
    )

    pengelola = PengelolaPengeluaran()
    pengelola.tambah_transaksi(transaksi1, transaksi2)

    # Lambda untuk mengurutkan transaksi berdasarkan nominal
    urutkan = lambda transaksi: transaksi.nominal
    pengelola.transaksi.sort(key=urutkan)

    ringkasan = pengelola.buat_ringkasan(pemilik="Pengguna")

    pengelola.tampilkan_semua()
    print("Total:", format_rupiah(ringkasan["total_pengeluaran"]))