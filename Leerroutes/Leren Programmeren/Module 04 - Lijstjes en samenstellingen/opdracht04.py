from fruitmand import fruitmand
import random

aantal = int(input("Hoeveel fruit wil je pakken? "))
for x in range(0, aantal):
    random_fruit = random.choice(fruitmand)
    print(random_fruit['name'])