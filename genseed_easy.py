#!/usr/bin/env python3
import random
import os
from tqdm import tqdm

# Konfigurasi
WORDLIST_FILE = 'frasa_2048.txt'
OUTPUT_FILE = 'daftar_seed.txt'
JUMLAH_SEED = 1000 # Ganti sesuai kebutuhan
PANJANG_KATA = 12   # 12, 15, 18, 21, atau 24

print("Memuat wordlist...")
with open(WORDLIST_FILE, 'r') as f:
    words = [line.strip() for line in f if line.strip()]

print(f"Total kata: {len(words)}")
print(f"Menghasilkan {JUMLAH_SEED} seed phrase...")
print(f"Menyimpan ke {OUTPUT_FILE}")

# Langsung tulis ke file
with open(OUTPUT_FILE, 'w') as f:
    for _ in tqdm(range(JUMLAH_SEED), ascii=True):
        seed = ' '.join(random.choices(words, k=PANJANG_KATA))
        f.write(seed + '\n')

# Hitung ukuran file
size = os.path.getsize(OUTPUT_FILE)
print("\n=== SELESAI ===")
print(f"File: {OUTPUT_FILE}")
print(f"Jumlah seed: {JUMLAH_SEED}")
print(f"Ukuran: {size:,} bytes ({size/1024:.2f} KB)")