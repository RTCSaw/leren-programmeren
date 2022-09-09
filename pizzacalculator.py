from msilib import MSIMODIFY_DELETE


pizza_klein =  5.99
pizza_middel =  10.99
pizza_groot =   12.99


pizza_klein_input = int (input ("Aantal kleine pizza's 26cm : "))
pizza_middel_input = int (input("aantal middel pizza's 30cm : "))
pizza_groot_input = int (input("aantal grote pizza's 35 cm: "))

pizza_klein_totaal = pizza_klein_input * 5.99
print("Kosten kleine pizza's",pizza_klein_totaal)

pizza_midden_totaal = pizza_middel_input * 10.99
print("kosten middengrote Pizza",pizza_midden_totaal)

pizza_groot_totaal = pizza_groot_input * 12.99
print("Kosten grote pizza's",pizza_groot_totaal)

alle_pizza_totaal = pizza_klein_totaal + pizza_midden_totaal + pizza_groot_totaal
print("Totale kosten: ", alle_pizza_totaal)

print("U heeft intotaal", pizza_klein_input, "kleine pizza's besteld,", pizza_middel_input, "midden grote pizza's besteld en ", pizza_groot_input , " grote pizza's besteld")
print("Dat komt op een totaal van", alle_pizza_totaal )