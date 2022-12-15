import random
namenlijst = []
namenlijst_shuffle = []
namen = 0
while namen<3:
    naam_input = input("Welke naam wilt u toevoegen?")
    if naam_input not in namenlijst:
        namenlijst.append(naam_input)
        namenlijst_shuffle.append(naam_input)
        namen +=1
    else:
        print("Deze naam heeft u al toegevoegd.")
    while namen >= 3:
        nog_een_naam = input("Wilt u nog een naam toevoegen?")
        if nog_een_naam =="ja":
                naam_input = input("Welke naam wilt u toevoegen?")
        else:
            break
        if naam_input not in namenlijst:
            namenlijst.append(naam_input)
            namenlijst_shuffle.append(naam_input)
        else:
            print("Deze naam heeft u al toegevoegd.")


for x in namenlijst_shuffle:
    random.shuffle(namenlijst_shuffle)
    for x in namenlijst_shuffle:
            print("test")
print(namenlijst)
print(namenlijst_shuffle)




