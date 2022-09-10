from msilib import MSIMODIFY_DELETE

# hier onder heb ik alle variable ingevoegd. de prijzen van de pizza's
pizza_klein =  5.99
pizza_middel =  10.99
pizza_groot =   12.99

# hier heb ik een user input toegevoegd om de persoon te laten bepalen hoeveel kleine, mmiddengrote en grote pizzas de persoon wilt bestellen
pizza_klein_input = int (input ("Aantal kleine pizza's 26cm : "))
pizza_middel_input = int (input("Aantal middel pizza's 30cm : "))
pizza_groot_input = int (input("Aantal grote pizza's 35 cm: "))

#hieronder wordt verwerkt dat het input van de user keer de prijs van de kleine,.....
pizza_klein_totaal = pizza_klein_input * 5.99
print("Kosten kleine pizza's",pizza_klein_totaal)
#de middengrote.....
pizza_midden_totaal = pizza_middel_input * 10.99
print("kosten middengrote Pizza",pizza_midden_totaal)
# en de grote pizza's berekend wordt.
pizza_groot_totaal = pizza_groot_input * 12.99
print("Kosten grote pizza's",pizza_groot_totaal)
#hier worden alle kosten bij elkaar opgeteld en geprint onder totale kosten
alle_pizza_totaal = pizza_klein_totaal + pizza_midden_totaal + pizza_groot_totaal

print("Totale kosten: ", alle_pizza_totaal)
# hier is een eind zin die de bestelling samenvat.
print("U heeft intotaal", pizza_klein_input, "kleine pizza's besteld,", pizza_middel_input, "midden grote pizza's besteld en ", pizza_groot_input , " grote pizza's besteld")
print("Dat komt op een totaal van", alle_pizza_totaal)