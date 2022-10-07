iphone = int(input("Wat is de prijs van de Iphone telefoon??"))
if iphone >=900:
    print("dit bedrag is te duur")
    iphone = int(input("Wat is de prijs van de Iphone telefoon??"))


samsung = int(input("Hoe Duur is de Samsung telefoon?"))
if samsung >=900:
    print("dit bedrag is te duur")
    samsung = int(input("Wat is de prijs van de Samsung telefoon??"))

asus = int(input("Hoe Duur is de Asus telefoon?"))
if asus >=900:
    print("dit bedrag is te duur")
    asus = int(input("Wat is de prijs van de Asus telefoon??"))



verschil1 = samsung - iphone 
verschil2 = iphone - samsung 
verschil3 = ((iphone > 100 , asus) and (samsung > 100 , asus))


if iphone >= samsung:
 
 print ("de iphone is het duurst, de telefoon kost",iphone,"Euro")
 print ("De samsung is het goedkoopst, De telefoon kost",samsung,"Euro")
 print("Het advies is dus de samsung te kopen, deze is namelijk",verschil2, "goedkoper" )


elif samsung >= iphone:
 print ("de samsung is het duurst, de telefoon kost",samsung,"Euro")
 print ("De iphone is het goedkoopst, De telefoon kost",iphone,"Euro")
 print("Het advies is dus de iphone te kopen, deze is namelijk",verschil1, "goedkoper" )  
elif samsung == iphone:
 print("Het advies ondanks dezelfde prijs de",iphone," te kopen, dit advies omdat u lichte voorkeur had naar iphone." )

elif verschil3 == True:
    print("De asus telefoon is 100 euro goedkoper")


if verschil1 <=50:
    print("de iphone is slechts", verschil1," duurder. Ik raadt u de iphone aan")


3