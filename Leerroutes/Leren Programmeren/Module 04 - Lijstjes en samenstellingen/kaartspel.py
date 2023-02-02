import random

nummer_kaarten = ("2","3","4","5","6","7","8","9","10","boer","vrouw","koning","aas")
soorten_kaarten = ("klaver","harten","schoppen","ruiten")
deck = []
teller = 0
for x in soorten_kaarten:
    for i in nummer_kaarten:
        deck.append(f"{x} {i}")

deck.append("jokerZ")
deck.append("jokerR")
random.shuffle(deck)
# print(deck)
for x in range(7):
    print (x +1, deck[0])
    deck.pop(0)   
print(deck)


