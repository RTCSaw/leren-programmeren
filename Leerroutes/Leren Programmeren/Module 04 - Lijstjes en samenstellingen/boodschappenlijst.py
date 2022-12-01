lijst ={}
toevoegen = True

while toevoegen:
    product = input("Welk product wilt u toevoegen? ").lower()
    while True:
        try:
            aantal_producten = int(input("hoeveel wilt u ervan toevoegen?"))
            break
        except:
            print("voeg een geldig nummer in")

    if product in lijst:
        lijst[product] += aantal_producten
    
    else:
        lijst.update({product : aantal_producten})

    while True:
        NogEen =  input("Wilt u nog een product toevoegen? ").lower()
        if NogEen in ["ja","j","jaa"]:
            break
        elif NogEen in ["nee","n"]:
            toevoegen = False
            break

print(f"Dit zijn uw boodschappen{lijst}")