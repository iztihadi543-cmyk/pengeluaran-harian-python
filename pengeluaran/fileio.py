# Modul untuk membaca dan menyimpan data pengeluaran

# Membuat file transaksi jika belum tersedia
def buat_file():
    try:
        with open("data/transaksi.txt", "x") as file:
            file.write("")
        print("File transaksi berhasil dibuat.")

    except FileExistsError:
        print("File transaksi sudah tersedia.")

# Menambahkan transaksi baru ke file
def tambah_data(transaksi):
    with open("data/transaksi.txt", "a") as file:
        file.write(
            f"{transaksi['tanggal']};"
            f"{transaksi['kategori']};"
            f"{transaksi['keterangan']};"
            f"{transaksi['nominal']}\n"
        )

# Membaca transaksi dari file
def baca_data():
    data = []

    try:
        with open("data/transaksi.txt", "r") as file:
            # Membaca file satu baris demi satu baris
            for baris in file:
                try:
                    bagian = baris.strip().split(";")

                    if len(bagian) != 4:
                        raise ValueError("Jumlah data tidak sesuai")

                    tanggal, kategori, keterangan, nominal = bagian

                    # Memeriksa data agar tidak kosong
                    if not tanggal or not kategori or not keterangan:
                        raise ValueError("Ada data yang kosong")

                    nominal = int(nominal)

                    if nominal <= 0:
                        raise ValueError("Nominal harus positif")

                    data.append({
                        "tanggal": tanggal,
                        "kategori": kategori,
                        "keterangan": keterangan,
                        "nominal": nominal
                    })

                except ValueError:
                    # Melewati baris yang rusak
                    print("Data rusak dilewati:", baris.strip())
                    continue

    except FileNotFoundError:
        print("File transaksi belum tersedia.")
        return []

    return data

# Menyimpan laporan pengeluaran ke file
def simpan_laporan(data, total):
    try:
        with open("laporan/laporan_pengeluaran.txt", "w") as file:
            file.write("LAPORAN PENGELUARAN HARIAN\n")
            file.write("==========================\n")
            file.write(f"Jumlah transaksi: {len(data)}\n")
            file.write(f"Total pengeluaran: Rp{total}\n\n")

            file.write("DAFTAR TRANSAKSI\n")

            for transaksi in data:
                file.write(
                    f"{transaksi['tanggal']} | "
                    f"{transaksi['kategori']} | "
                    f"{transaksi['keterangan']} | "
                    f"Rp{transaksi['nominal']}\n"
                )

        print("Laporan berhasil disimpan.")

    except OSError as error:
        print("Laporan gagal disimpan:", error)


# Pengujian sederhana jika modul dijalankan langsung
if __name__ == "__main__":
    buat_file()
    data = baca_data()
    print("Jumlah data:", len(data))