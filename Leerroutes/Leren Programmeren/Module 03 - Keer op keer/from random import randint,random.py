from random import randint,random

secret = randint (1,1000)

print (secret)
print(secret)
score = 0
while score != 10:
    guess = int(input("Welk getal denkt u dat het is? "))
    answer = secret - guess
    if secret == guess:
        print("U heeft het goed geraden")

    elif answer in range(20,50):
        print("U bent warm")

    elif answer in range(1,20):
        print("U bent erg warm")
    elif answer >50:
        print("niet in de buurt")
    score +=1
print("u heeft het 10 keer geprobeerd te raden. helaas heeeft u het getal niet geraden...")