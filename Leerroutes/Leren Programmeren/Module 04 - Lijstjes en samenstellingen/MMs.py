import random
kleuren = ("groen", "blauw","oranje","bruin")
hoeveel = int(input("hoeveel mms wil je?"))
bowl =[] 
while hoeveel !=0:
    bowl += random.sample(kleuren,1)
    hoeveel -=1
print(f"U heeft de volgende M&M's in de bowl{bowl}")


