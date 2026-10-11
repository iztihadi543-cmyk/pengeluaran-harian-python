# Sistem Pengelolaan Pengeluaran Harian

## Deskripsi

Program Python sederhana untuk mencatat, mengelola, dan menganalisis pengeluaran harian melalui terminal.

## Fitur

- Menambahkan transaksi pengeluaran.
- Menampilkan seluruh transaksi.
- Menghitung total pengeluaran.
- Menghitung pengeluaran berdasarkan kategori.
- Menyimpan laporan ke file teks.
- Memvalidasi input pengguna.
- Menguji fungsi program secara otomatis.

## Struktur Proyek

- `main.py`: program utama dan menu.
- `pengeluaran/__init__.py`: penanda package Python.
- `pengeluaran/validasi.py`: validasi transaksi.
- `pengeluaran/fileio.py`: membaca dan menyimpan file.
- `pengeluaran/processing.py`: pengolahan transaksi.
- `pengeluaran/testing.py`: pengujian otomatis.
- `data/`: penyimpanan transaksi.
- `laporan/`: penyimpanan laporan.

## Persyaratan

- Python 3.
- Tidak membutuhkan instalasi pustaka tambahan.

## Cara Menjalankan

Jalankan perintah berikut dari folder proyek:

```bash
python main.py
```

## Cara Menjalankan Pengujian

```bash
python -m unittest pengeluaran.testing -v
```

## Format Data Transaksi

Data transaksi disimpan dengan format berikut:

`Tanggal;Kategori;Keterangan;Nominal`

Contoh:

`11-10-2026;Makanan;Makan siang;15000`

## Mata Kuliah

Pemograman Terstruktur