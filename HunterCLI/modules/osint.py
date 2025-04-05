import requests

platforms = {
    "GitHub": "https://github.com/{}",
    "Instagram": "https://www.instagram.com/{}",
    "Twitter": "https://twitter.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "Pinterest": "https://www.pinterest.com/{}/",
    "Tumblr": "https://{}.tumblr.com/",
    "TikTok": "https://www.tiktok.com/@{}"
}

def check_username(username):
    print(f"🔍 Mencari jejak username: {username}\n")
    for name, url in platforms.items():
        try:
            response = requests.get(url.format(username), timeout=5)
            if response.status_code == 200:
                print(f"  ✅ Ditemukan di {name}: {url.format(username)}")
            elif response.status_code == 404:
                print(f"  ❌ Tidak ditemukan di {name}")
            else:
                print(f"  ⚠️  {name}: Status tidak dikenal ({response.status_code})")
        except requests.exceptions.RequestException:
            print(f"  ⚠️  Gagal mengakses {name}")
