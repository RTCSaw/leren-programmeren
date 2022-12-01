from operator import truediv

dageninweek = ""
inputdag = input("Welke dag is het vandaag, ma/di/wo/do/vr/za/zo: ")

while inputdag != dageninweek:
    if dageninweek == "":
        dageninweek = "ma"
    elif dageninweek == "ma":
        dageninweek = "di"
    elif dageninweek == "di":
        dageninweek = "wo"
    elif dageninweek == "wo":
        dageninweek = "do"
    elif dageninweek == "do":
        dageninweek = "vr"
    elif dageninweek == "vr":
        dageninweek = "za"
    elif dageninweek == "za":
        dageninweek = "zo"
    else:
        break
    print (dageninweek)


