import requests
def check_wallet(phone_number):
    print(f"💸 Cek e-Wallet untuk nomor: {phone_number}\n")

    headers = {
        "Content-Type": "application/json"
    }

    # Cek OVO via API simulasi (form top-up OVO pada merchant)
    try:
        url = "https://api.danacita.co.id/validate-phone"  # contoh dummy (ganti jika punya sumber asli)
        payload = {"phone": phone_number}
        res = requests.post(url, json=payload, headers=headers, timeout=5)
        if res.status_code == 200:
            print("  ✅ Terdaftar di DANA (simulasi valid response)")
        else:
            print("  ❌ Tidak terdeteksi di DANA (status:", res.status_code, ")")
    except Exception as e:
        print("  ⚠️  Gagal cek ke DANA:", str(e))

    # OVO, ShopeePay, dan lainnya bisa ditambahkan kemudian
