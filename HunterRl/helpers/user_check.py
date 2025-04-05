def check_username(username):
    print(f"🔎 Mencari akun '{username}' di platform populer...")
    found = []
    fake_db = {
        "instagram": ["budi123", "john_doe", "hunterx"],
        "github": ["john_doe", "devman99", "hunterx"]
    }

    for platform, users in fake_db.items():
        if username in users:
            found.append(platform)

    if found:
        for plat in found:
            print(f"  ✅ Ditemukan di {plat}")
    else:
        print("  ❌ Tidak ditemukan di platform manapun")
