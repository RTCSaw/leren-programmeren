from time import time


uur = int (input ("Wat is de huidige tijd in uren? "))
minuten = int (input ("Wat is de huidige tijd in minuten"))


hele_dag_uur = 23 - uur
hele_dag_min = 60 - minuten

print(hele_dag_uur)
print(hele_dag_min)
print("nog", hele_dag_uur , "uur en nog", hele_dag_min ,"tot het einde van de dag")