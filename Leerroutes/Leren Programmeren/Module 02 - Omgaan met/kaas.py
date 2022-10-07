

geel = input ('Is de kaas geel? ')
if geel == "nee":
     print(' ')
 
     schimmel = input("Heeft de kaas blauwe schimmel? ")
     if schimmel == "nee":
        print('')

        korst = input ("Heeft de kaas een korst? ")
        if korst == "nee":
         print("Mozzeralla")
        elif korst == "ja":
            print("Camembert")

     elif schimmel == "ja":
        print("")

        korst1 = input("Heeft de kaas een korst? ")
        if korst1 == "ja":
             print("Blue de Rochbaron")
        elif korst1 == "nee":
                 print("Foume d'Ambert")
elif geel == "ja":
    print("")

    gaten = input("Zitten er in de kaas gaten?")
    if gaten == "nee":
     print("")

     steen = input("is de kaas zo hard als steen? ")
     if steen == "ja":
        print("parmigiano Reggiano")
        
     elif steen == "nee":
        print("Goudse Kaas")
    
    elif gaten == "ja":
        print("")

        duur = input("Is de kaas erg duur? ")
        if duur == "ja":
            print("Emmenthaler")
        elif duur == "nee":
            print("Leerdammer")



