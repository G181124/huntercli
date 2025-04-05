import argparse
from helpers.phone_check import check_phone
from helpers.nik_check import check_nik
from helpers.user_check import check_username

def main():
    parser = argparse.ArgumentParser(description="HunterNum CLI OSINT Tool")
    parser.add_argument("--phone", help="Cek nomor HP")
    parser.add_argument("--nik", help="Cek NIK")
    parser.add_argument("--username", help="Cek username di platform populer")
    args = parser.parse_args()

    if args.phone:
        check_phone(args.phone)
    if args.nik:
        check_nik(args.nik)
    if args.username:
        check_username(args.username)

if __name__ == "__main__":
    main()
