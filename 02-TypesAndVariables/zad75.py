blachy = input("Podaj blachy auta: ")
czykrk = blachy[0:2] == "KR" or blachy[0:2] == "KK"
print(f"Czy są to blachy z Krakowa? {czykrk}")