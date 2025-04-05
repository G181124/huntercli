def check_phone(phone):
    print("📱 Info Nomor Telepon:")
    if phone.startswith("0812") or phone.startswith("0813"):
        print("  - Provider: Telkomsel")
    elif phone.startswith("0857") or phone.startswith("0856"):
        print("  - Provider: Indosat")
    elif phone.startswith("0821") or phone.startswith("0822"):
        print("  - Provider: XL")
    else:
        print("  - Provider: Tidak diketahui")
