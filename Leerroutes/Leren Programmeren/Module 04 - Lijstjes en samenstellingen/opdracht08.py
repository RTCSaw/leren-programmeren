from fruitmand import fruitmand
watermeloen = {
    'name' : 'watermeloen',
    'weight' : 780,
    'color' : 'green',
    'round' : True
}
fruitmand.append(watermeloen)

totaal_gewicht = 0
for fruit in fruitmand:                                          
    totaal_gewicht += fruit["weight"]
print(f"{totaal_gewicht} gram")
