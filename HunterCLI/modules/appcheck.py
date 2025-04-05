import requests

def check_app(phone):
    print(f"📦 Cek aplikasi dengan nomor: {phone}\n")

    try:
        # Simulasi validasi no HP di Tokopedia (contoh endpoint)
        url = "https://example.com/check-app"  # ← placeholder
        response = requests.post(url, json={"phone": phone}, timeout=5)

        if response.status_code == 200:
            print("  ✅ Nomor terdaftar di aplikasi")
        elif response.status_code == 404:
            print("  ❌ Nomor tidak ditemukan")
        else:
            print(f"  ⚠️ Status tidak dikenal: {response.status_code}")
    except Exception as e:
        print("  ⚠️  Gagal mengakses data aplikasi:", str(e))
