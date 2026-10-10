
# Modul untuk menguji program pengeluaran harian

import unittest

from pengeluaran.processing import (
    Transaksi,
    PengelolaPengeluaran,
    format_rupiah
)
from pengeluaran.validasi import (
    validasi_transaksi,
    DataError
)


# Class untuk menjalankan pengujian program
class TestPengeluaran(unittest.TestCase):

    # Menyiapkan objek sebelum setiap pengujian
    def setUp(self):
        self.pengelola = PengelolaPengeluaran()

        self.transaksi1 = Transaksi(
            "11-10-2026",
            "Makanan",
            "Makan siang",
            15000
        )

        self.transaksi2 = Transaksi(
            "11-10-2026",
            "Transportasi",
            "Ongkos",
            10000
        )

    # Menguji penambahan transaksi
    def test_tambah_transaksi(self):
        self.pengelola.tambah_transaksi(self.transaksi1)

        self.assertEqual(len(self.pengelola.transaksi), 1)

    # Menguji perhitungan total pengeluaran
    def test_hitung_total(self):
        self.pengelola.tambah_transaksi(
            self.transaksi1,
            self.transaksi2
        )

        self.assertEqual(self.pengelola.hitung_total(), 25000)

    # Menguji total pengeluaran berdasarkan kategori
    def test_total_kategori(self):
        self.pengelola.tambah_transaksi(
            self.transaksi1,
            self.transaksi2
        )

        self.assertEqual(
            self.pengelola.total_kategori("Makanan"),
            15000
        )

    # Menguji format rupiah
    def test_format_rupiah(self):
        self.assertEqual(format_rupiah(25000), "Rp25.000")

    # Menguji validasi transaksi yang benar
    def test_validasi_transaksi_valid(self):
        data = validasi_transaksi(
            "11-10-2026",
            "Makanan",
            "Makan siang",
            15000
        )

        self.assertEqual(data["nominal"], 15000)

    # Menguji penolakan nominal negatif
    def test_nominal_negatif_ditolak(self):
        with self.assertRaises(DataError):
            validasi_transaksi(
                "11-10-2026",
                "Makanan",
                "Makan siang",
                -15000
            )


# Menjalankan pengujian jika file dibuka langsung
if __name__ == "__main__":
    unittest.main()
