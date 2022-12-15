from random import randint
landen_lijst = []
teller = 1
while teller <=3:
    landen = input("welke landen spelen in groep A? ")
    if landen in landen_lijst:
        print("dit land is al toegevoegd. ")
    else:
        landen_lijst.append(landen)
        teller +=1
print(landen_lijst)

