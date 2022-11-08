# name of student: Sam Hulsbergen
# number of student: 99065436
# purpose of program: 
# function of program: 
# structure of program:  


toPay = int(float(input('Amount to pay: '))* 100) # hier wordt gevraagd at je moet betalen, vervolgens wordt het keer 100 gedan zodat het in centen komt.
paid = int(float(input('Paid amount: ')) * 100) # hier wordt gevraagd wat je betaald hebt en dat wordt ook keer 100 gedaan om het in centen te zetten.
change = paid - toPay # change is het wisselgeld, paid is het bedrg wat de gebruiker betaald heeft. to pay is het bedrag dat moet betaald worden. 
#door paid - topay te rekenen wordt het verschil berekend, dit is je wisselgeld
toprint = ""

if change > 0: # deze if wordt geactiveerd als de change variable meer dan 0 is
  coinValue = 500 # De coin value wordt gelijl gekent aan 500, dit wotdt pas later in de code meer belangerijk ivm wisselgeld terug geven
  
  while change > 0 and coinValue > 0: #deze code werkt alsvolgt: als change groter is dan 0 EN coinvalue hoger is dan 0
  #dan komt er een nieuwe variable "nrCoins die er voor zorggt dat nrcoins change is dat geleed door wordt door coinvalue die afgerond wordt naar beneden.
  # dit zorgt ervoor dat de software kan zien hoeveel er bijvoorbeeld 50 centen in 140 cent past. dit rind hij af naar onder en het antwoordzal 2 zijn"
    nrCoins = change // coinValue 

    if nrCoins > 0: #
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) #
      change -= nrCoinsReturned * coinValue #
      totalReturned = nrCoinsReturned
      totalValue = coinValue
      toprint += f"coins returned: {totalReturned} van {totalValue} cents\n"

# comment on code below: 
# De computer maakt van al deze code hieronder een soort deelsom. eerste kijkt de terminal van hoevaak past de 146 cent in de 500 cent. dat is 0 keer
# vervolgens gaat hij naar 300. dit is ook 0. dan naar 200 en dat blijkt ook 0 te zijn. vervolgens komt hij bij 50. dan kan het ineens wel. van de 146 kan 
#de 50 daar 2x helemaal in. er blijft dus 46 over. die gaat door naar de volgende tot het hele getal op is.
    if coinValue == 500:
      coinValue = 300
    elif coinValue == 300:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0
print (nrCoinsReturned)
if change > 0: # dit wordt getriggerd als de change neit vermeld staat of te klein is.
  print('Change not returned: ', str(change) + ' cents')
else:
  print(toprint)