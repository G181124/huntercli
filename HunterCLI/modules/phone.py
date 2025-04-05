def check_phone(phone):
    print("📱 Info Nomor Telepon:")

    prefix = phone[:4]

    telkomsel = {"0811", "0812", "0813", "0821", "0822", "0852", "0853", "0823", "0851"}
    indosat = {"0855", "0856", "0857", "0858", "0814", "0815", "0816"}
    xl = {"0817", "0818", "0819", "0859", "0877", "0878"}
    tri = {"0895", "0896", "0897", "0898", "0899"}
    smartfren = {"0881", "0882", "0883", "0884", "0885", "0886", "0887", "0888", "0889"}

    if prefix in telkomsel:
        provider = "Telkomsel"
    elif prefix in indosat:
        provider = "Indosat"
    elif prefix in xl:
        provider = "XL Axiata"
    elif prefix in tri:
        provider = "Tri (3)"
    elif prefix in smartfren:
        provider = "Smartfren"
    else:
        provider = "Tidak diketahui"

    print(f"  - Provider: {provider}")
