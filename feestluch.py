from re import T


croissantjes = int(input ('Hoeveel croissantjes wilt u?'))
croistotaal = croissantjes * 0.39
stokbrood = int(input("hoeveel stokbroden wilt u?"))
stokbrTotaal = stokbrood * 2.78
aantal_kortingsbonnen = int(input (" (Hoeveel kortingsbonnen heeft u?"))
korting = int(input ("hoeveel cent zijn ze waard?"))
korting_totaal = aantal_kortingsbonnen * korting / 100

totaal= stokbrTotaal + croistotaal - korting_totaal

print("De feestlunch kost je bij de bakker ",{totaal}," euro voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn!")