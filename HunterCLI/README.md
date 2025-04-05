# HunterCLI v2 - OSINT CLI Tool

HunterCLI adalah tool OSINT berbasis command line untuk melakukan pencarian informasi publik, seperti nomor HP, NIK, username, rekening bank, e-wallet, dan aplikasi marketplace.

## 📦 Fitur

- `--phone`     : Deteksi provider berdasarkan nomor HP
- `--nik`       : Parsing dan validasi data dari NIK
- `--osint`     : Cari jejak username di platform populer
- `--wallet`    : Cek apakah nomor terdaftar di OVO/DANA
- `--bank`      : Validasi nomor rekening (simulasi endpoint)
- `--appcheck`  : Cek apakah nomor digunakan di aplikasi (contoh: Tokopedia)

## 🛠 Instalasi

```bash
git clone https://github.com/username/HunterCLI.git
cd HunterCLI
chmod +x install.sh
./install.sh
source ~/.bashrc   # atau ~/.zshrc tergantung shell kamu
```

## 🧪 Contoh Penggunaan

```bash
huntercli --phone 081234567890
huntercli --nik 3201010101010001
huntercli --osint hunterx
huntercli --wallet 085777777777
huntercli --bank 1234567890
huntercli --appcheck 081234567890
```

## ⚠️ Catatan

Tool ini hanya mengambil data dari sumber yang legal & publik. Tidak ada database ilegal atau scraping ke sistem pemerintah. Beberapa endpoint bersifat simulasi untuk keperluan edukasi.

