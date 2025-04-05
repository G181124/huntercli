import requests

def check_bank(rek):
    print(f"🏦 Validasi Rekening: {rek}\n")

    try:
        # Simulasi endpoint validasi (gunakan form/topup bank real jika tersedia)
        url = "https://example.com/validate-bank"  # ← placeholder
        response = requests.post(url, json={"account": rek}, timeout=5)

        if response.status_code == 200:
            print("  ✅ Nomor rekening valid dan dikenali")
        else:
            print(f"  ❌ Tidak terverifikasi (status {response.status_code})")
    except Exception as e:
        print("  ⚠️  Gagal menghubungi server bank:", str(e))
