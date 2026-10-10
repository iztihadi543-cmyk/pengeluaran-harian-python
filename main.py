# Program utama Sistem Pengelolaan Pengeluaran Harian

from pengeluaran.validasi import validasi_transaksi, DataError
from pengeluaran.fileio import (
    buat_file,
    tambah_data,
    baca_data,
    simpan_laporan
)
from pengeluaran.processing import (
    Transaksi,
    PengelolaPengeluaran,
    format_rupiah
)


# Menampilkan menu utama program
def tampilkan_menu():
    print("\n=== PENGELOLAAN PENGELUARAN HARIAN ===")
    print("1. Tambah pengeluaran")
    print("2. Lihat semua pengeluaran")
    print("3. Lihat total pengeluaran")
    print("4. Lihat total berdasarkan kategori")
    print("5. Simpan laporan")
    print("0. Keluar")


# Membaca data file dan memasukkannya ke objek pengelola
def muat_pengeluaran():
    pengelola = PengelolaPengeluaran()

    for data in baca_data():
        transaksi = Transaksi(
            data["tanggal"],
            data["kategori"],
            data["keterangan"],
            data["nominal"]
        )
        pengelola.tambah_transaksi(transaksi)

    return pengelola


# Meminta input dan menyimpan transaksi baru
def menu_tambah():
    try:
        tanggal = input("Tanggal (DD-MM-YYYY): ")
        kategori = input("Kategori: ")
        keterangan = input("Keterangan: ")
        nominal = input("Nominal (Rp): ")

        data = validasi_transaksi(
            tanggal,
            kategori,
            keterangan,
            nominal
        )

        tambah_data(data)
        print("Pengeluaran berhasil ditambahkan.")

    except DataError as error:
        print("Data tidak valid:", error)

    except (ValueError, OSError) as error:
        print("Terjadi kesalahan:", error)


# Menampilkan semua transaksi yang tersimpan
def menu_lihat():
    pengelola = muat_pengeluaran()

    if not pengelola.transaksi:
        print("Belum ada data pengeluaran.")
        return

    print("\n=== DAFTAR PENGELUARAN ===")
    pengelola.tampilkan_semua()


# Menampilkan total seluruh pengeluaran
def menu_total():
    pengelola = muat_pengeluaran()
    total = pengelola.hitung_total()

    print("Total pengeluaran:", format_rupiah(total))


# Menampilkan total berdasarkan kategori pilihan
def menu_kategori():
    pengelola = muat_pengeluaran()
    kategori = input("Masukkan kategori: ")

    total = pengelola.total_kategori(kategori)

    print(
        f"Total kategori {kategori}: "
        f"{format_rupiah(total)}"
    )


# Menyimpan laporan pengeluaran ke file
def menu_laporan():
    data = baca_data()
    pengelola = muat_pengeluaran()
    total = pengelola.hitung_total()

    simpan_laporan(data, total)


# Menjalankan menu sampai pengguna memilih keluar
def main():
    buat_file()

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            menu_tambah()

        elif pilihan == "2":
            menu_lihat()

        elif pilihan == "3":
            menu_total()

        elif pilihan == "4":
            menu_kategori()

        elif pilihan == "5":
            menu_laporan()

        elif pilihan == "0":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


# Menjalankan program utama
if __name__ == "__main__":
    main()
