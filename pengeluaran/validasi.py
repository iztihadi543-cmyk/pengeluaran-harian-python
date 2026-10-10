# Modul untuk memeriksa data pengeluaran
from datetime import datetime

# Exception khusus untuk data yang salah
class DataError(ValueError):
    pass

# Memeriksa tanggal, kategori, keterangan, dan nominal
def validasi_transaksi(tanggal, kategori, keterangan, nominal):
    # Memeriksa format dan kebenaran tanggal
    try:
        tanggal_valid = datetime.strptime(tanggal, "%d-%m-%Y")

        if tanggal_valid.strftime("%d-%m-%Y") != tanggal:
            raise DataError("Format tanggal harus DD-MM-YYYY!")

    except ValueError:
        raise DataError("Tanggal tidak valid!") from None

    # Memeriksa kategori dan keterangan agar tidak kosong
    if not kategori.strip():
        raise DataError("Kategori tidak boleh kosong!")

    if not keterangan.strip():
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