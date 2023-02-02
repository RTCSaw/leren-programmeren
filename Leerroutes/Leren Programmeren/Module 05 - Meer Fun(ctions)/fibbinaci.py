def fibonacci():
    a, b = 0, 1
    teller = 0
    getallenlijst = []
    aantal_nummers = int(input("hoeveel nummers wilt u berekenen? "))
    while teller < aantal_nummers:
        print(a)
        getallenlijst.append(a)
        new = a + b
        a = b
        b = new
        teller +=1
    lengte = len(getallenlijst) 
    print(f"De laatste 2 getallen delen door elkaar is: {getallenlijst [lengte-1]} / {getallenlijst [lengte-2]}")

fibonacci()