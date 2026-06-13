# Simple Seed Phrase Generator

Sebuah skrip Python sederhana, cepat, dan ringan untuk menghasilkan *seed phrase* (frasa mnemorik) acak secara massal (*bulk*) dari daftar kata (*wordlist*) kustom. Skrip ini dirancang untuk kebutuhan pengujian, simulasi kriptografi, atau pembuatan data acak berbasis teks.

## ✨ Fitur Utama

* **Generasi Massal Cepat:** Mampu menghasilkan ribuan *seed phrase* dalam hitungan detik menggunakan alokasi memori yang efisien (langsung menulis ke file).
* **Kustomisasi Panjang Kata:** Mendukung konfigurasi panjang frasa standar (12, 15, 18, 21, atau 24 kata).
* **Indikator Progres visual:** Menggunakan `tqdm` untuk menampilkan *progress bar* interaktif secara real-time di terminal.
* **Ringkasan Output:** Menampilkan informasi ukuran file akhir dalam format byte dan Kilobyte (KB) setelah proses selesai.

## 🚀 Prasyarat

Sebelum menjalankan skrip ini, pastikan Anda sudah menginstal Python 3 dan pustaka pendukung:

```bash
pip install tqdm
