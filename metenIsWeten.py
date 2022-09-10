a = int (input("kies een getal voor variable a "))
b = int (input("kies een getal voor varialble b "))

if b > a:

  max = b
  min = a
  print("b is groter dan a met een waarde van ", max,"tegen", min)

elif a == b:
  print("a and b are equal")
else:
  
  print("a is greater than b")
  max = a
  min = b

  print("a is groter dan b met een waarde van ", max,"tegen", min)
  