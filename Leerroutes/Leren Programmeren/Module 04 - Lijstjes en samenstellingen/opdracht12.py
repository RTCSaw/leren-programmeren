from fruitmand import fruitmand
aantal_characters = 0                                               # aantal char heeft een standaard waarde van 0
fruitnamen = []                                     
for x in range(0, len(fruitmand)):                                  # De loop gaat door de lengte van fruitmand
    namenlijst = len(fruitmand[x].get('name'))                      # namenlijst wordt 
    if namenlijst > aantal_characters:
        aantal_characters = namenlijst

for x in range(0, len(fruitmand)):
    if aantal_characters == len(fruitmand[x].get('name')):
        fruitnaam = fruitmand[x].get('name')
        gewicht = fruitmand[x].get('weight')/1000
        kleur = fruitmand[x].get('color')
        break

vertalingdict =  {
    'red' : 'rode',
    'green' : 'groene',
    'orange': 'orangje',
    'yellow' : 'gele',
    'brown' : "bruine",
}

print(f"De '{fruitnaam}'' ({aantal_characters}) letters heeft een {kleur} kleur en een gewicht van {gewicht}")