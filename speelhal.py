# Dat kost een toegangsticket per persoon van 7,45 euro voor de hele dag. Jullie willen ook met zijn allen voor 45 minuten in de VIP-VR-GameSeat. De VIP-VR GameSeat kost per persoon 37 eurocent per 5 minuten. Jij trakteert dus betaal je alles
ticket = 7.45
ticketkosten = ticket * 3
print("Kosten toegang gamehall: ", ticketkosten)

virtualrealitypp = 0.37 * 9
print('Virtual reality kosten per persoon: ',virtualrealitypp)
totalvrcost = virtualrealitypp * 3 
print("Totale kosten Virtual reality:", totalvrcost)

TotalCost = totalvrcost + ticketkosten
print("de totalen kosten voor de gamehall is ", TotalCost)