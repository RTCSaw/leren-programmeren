from operator import itemgetter
from fruitmand import fruitmand
fruitmand = sorted(fruitmand , key = itemgetter('weight'), reverse=True)
print(fruitmand)
for fruit in fruitmand: 
    print(fruit['weight'], fruit['name'])

    #lambda checken voor int en str compares