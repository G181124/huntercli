import json
from datetime import datetime

def check_nik(nik):
    print("🆔 Info NIK:")
    if len(nik) != 16 or not nik.isdigit():
        print("  - ❌ NIK tidak valid (harus 16 digit angka)")
        return

    kode_wilayah = nik[:6]
    tanggal_lahir = nik[6:12]
    
    try:
        hari = int(tanggal_lahir[:2])
        bulan = int(tanggal_lahir[2:4])
        tahun = int(tanggal_lahir[4:6])
        if hari > 40:
            hari -= 40  # menandakan perempuan
        tahun += 1900 if tahun > 25 else 2000  # asumsi tahun >25 berarti kelahiran 1900-an

        tanggal = datetime(tahun, bulan, hari).strftime('%d-%m-%Y')
    except:
        tanggal = "❌ Tidak bisa membaca tanggal lahir"

    try:
        with open("data/wilayah.json") as f:
            data = json.load(f)
            wilayah = data.get(kode_wilayah, "Wilayah tidak ditemukan")
    except:
        wilayah = "❌ Gagal membaca file wilayah"

    print(f"  - Kode Wilayah: {kode_wilayah} ({wilayah})")
    print(f"  - Tanggal Lahir: {tanggal}")
