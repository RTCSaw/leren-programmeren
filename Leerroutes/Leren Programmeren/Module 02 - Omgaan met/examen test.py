scoreE = int (input("Vul een getal van minimaal 0 en maximaal 6 in"))
scoreE <= 6

scoreP = int(input("Vul een getal van minimaal 0 en maximaal 8"))
scoreP <= 8

scoreO = int (input("Vul een getal van minimaal 0 en maximaal 5 in"))
scoreO <= 5

scoreS = int(input("Vul een getal van minimaal 0 en maximaal 2 in"))
scoreS <= 2
    

totale_score = scoreE + scoreP - scoreO - scoreS

if scoreP == 8 and scoreE >= 4 and scoreO == 0 and scoreS == 0:
    print("De uitslag is goed!")

elif (scoreS == 0 and totale_score >=7 and totale_score < 13 ) or (scoreS == 1 and totale_score >= 9):
    print("de score is voldoende!")

else :
 print("U heeft helaas een onvoldoende")
