import argparse
from modules.phone import check_phone
from modules.nik import check_nik
from modules.osint import check_username
from modules.wallet import check_wallet
from modules.bank import check_bank
from modules.appcheck import check_app

def main():
    parser = argparse.ArgumentParser(description="HunterCLI v2 - OSINT Tool")
    parser.add_argument("--phone", help="Cek provider nomor HP (08xxxx)")
    parser.add_argument("--nik", help="Analisis & parsing NIK (16 digit)")
    parser.add_argument("--osint", help="Cari jejak digital username di berbagai platform")
    parser.add_argument("--wallet", help="Cek apakah nomor HP terdaftar di e-wallet OVO/DANA")
    parser.add_argument("--bank", help="Validasi nomor rekening di sistem pembayaran")
    parser.add_argument("--appcheck", help="Cek nomor HP terdaftar di aplikasi seperti Tokopedia")

    args = parser.parse_args()

    if args.phone:
        check_phone(args.phone)

    if args.nik:
        check_nik(args.nik)

    if args.osint:
        check_username(args.osint)

    if args.wallet:
        check_wallet(args.wallet)

    if args.bank:
        check_bank(args.bank)

    if args.appcheck:
        check_app(args.appcheck)

if __name__ == "__main__":
    main()