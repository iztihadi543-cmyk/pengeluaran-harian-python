# Modul untuk memeriksa data pengeluaran


# Exception khusus untuk data yang salah
class DataError(ValueError):
    pass


# Memeriksa data transaksi sebelum disimpan
def validasi_transaksi(tanggal, kategori, keterangan, nominal):
    # Memeriksa format tanggal DD-MM-YYYY
    if not isinstance(tanggal, str):
        raise DataError("Tanggal harus berupa teks!")

    bagian_tanggal = tanggal.split("-")

    if len(bagian_tanggal) != 3:
        raise DataError("Format tanggal harus DD-MM-YYYY!")

    try:
        hari = int(bagian_tanggal[0])
        bulan = int(bagian_tanggal[1])
        tahun = int(bagian_tanggal[2])
    except ValueError:
        raise DataError("Tanggal harus menggunakan angka!") from None

    # Memeriksa batas tanggal dan bulan secara sederhana
    if tahun < 1 or bulan < 1 or bulan > 12:
        raise DataError("Tanggal tidak valid!")

    jumlah_hari = [31, 29 if tahun % 4 == 0 else 28,
                   31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if hari < 1 or hari > jumlah_hari[bulan - 1]:
        raise DataError("Tanggal tidak valid!")

    # Memastikan format menggunakan dua digit hari dan bulan
    if tanggal != f"{hari:02d}-{bulan:02d}-{tahun:04d}":
        raise DataError("Format tanggal harus DD-MM-YYYY!")

    # Memeriksa kategori dan keterangan
    if not isinstance(kategori, str) or not kategori.strip():
        raise DataError("Kategori tidak boleh kosong!")

    if not isinstance(keterangan, str) or not keterangan.strip():
        raise DataError("Keterangan tidak boleh kosong!")

    # Memeriksa nominal harus berupa bilangan bulat
    try:
        nominal = int(nominal)
    except (ValueError, TypeError):
        raise DataError("Nominal harus berupa angka bulat!") from None

    # Nominal harus lebih dari nol
    if nominal <= 0:
        raise DataError("Nominal harus lebih dari nol!")

    # Memastikan nominal yang diterima positif
    assert nominal > 0

    # Mengembalikan data yang sudah diperiksa
    return {
        "tanggal": tanggal,
        "kategori": kategori.strip(),
        "keterangan": keterangan.strip(),
        "nominal": nominal
    }


# Pengujian lokal jika file dijalankan langsung
if __name__ == "__main__":
    try:
        data = validasi_transaksi(
            "11-10-2026",
            "Makanan",
            "Makan siang",
            15000
        )
        print("Data valid:", data)

    except DataError as error:
        print("Kesalahan:", error)