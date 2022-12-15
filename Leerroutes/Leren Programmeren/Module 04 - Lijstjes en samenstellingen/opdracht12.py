from fruitmand import fruitmand
vertaling =  {                                                      # alles eerst vertaald door middel van een dict.
                                                                    # dubbele punt staat voor red is nu rode enzv
    'red' : 'rode',
    'green' : 'groene',
    'orange': 'orangje',
    'yellow' : 'gele',
    'brown' : "bruine",
}

aantal_characters = 0   
long_fruit = fruitmand[0]                                                   # aantal char heeft een standaard waarde van 0                                   
for fruit in fruitmand:                                       # De loop gaat door de lengte van fruitmand                       # hier wordt de fruitnaam uit de dict gehaald en de variable naam fruitnaam gekoppeld                       
    if len(fruit['name'])  > len(long_fruit['name']):                                     # Als fruitnaam meer karakters heeft dan aantal karakters, dan wordt
        long_fruit = fruit                                   # aantal karakers aan fruitnaam gekoppeld, dus hier wordt gecheckt welke naam
                                                                           # de meeste letters heeft.                                                                                                                                          
                                                                          # De print die alles uitprint
print(f"De '{long_fruit['name']}' ({len(long_fruit['name'])} letters) heeft een {long_fruit['color']} kleur en een gewicht van {long_fruit['weight']} kg")