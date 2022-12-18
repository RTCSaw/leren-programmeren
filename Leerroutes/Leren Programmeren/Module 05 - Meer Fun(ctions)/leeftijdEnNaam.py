def naam_en_leeftijd():
    gegevens_lijst = []
    while True:
        naam = input("Welke naam wilt u toevoegen? ")
        if naam =="stop":
            break
        leeftijd = int(input(f"Hoe oud is {naam} "))
        gegevens_lijst.append((naam, leeftijd))
        
    for naam, leeftijd in gegevens_lijst:
        print(f"{naam} is {leeftijd} jaar")

naam_en_leeftijd()
    
