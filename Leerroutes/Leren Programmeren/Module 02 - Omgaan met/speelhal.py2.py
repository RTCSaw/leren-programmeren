ticket = 7.45
ticketkosten = ticket * int(input("Met hoeveel personen wilt u naar de gamehal?"))


virtualrealitypp = int(input ("hoeveel minuten wilt VRen?") )
kosten_per_minuut = 0.074
kosten_vr = virtualrealitypp * kosten_per_minuut

kosten_vr_AF = round (kosten_vr,2)
print('Virtual reality kosten per persoon: ',kosten_vr_AF)
totalvrcost = kosten_vr_AF * 4 
print("Totale kosten Virtual reality:", {totalvrcost})

print("Kosten toegang gamehall: ", ticketkosten)
TotalCost = totalvrcost + ticketkosten
afgrondtotaal= round (TotalCost,2)
afgrondtotaal *= 100
print("de totalen kosten voor de gamehall is ", {afgrondtotaal})
print("Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar" ,{afgrondtotaal})