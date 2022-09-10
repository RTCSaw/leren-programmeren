a = int (input("kies een getal voor variable a "))
b = int (input("kies een getal voor varialble b "))

if b > a:

  max = b
  min = a
  print("het minimum is ",a , "Het maximum is",b)

elif a == b:
  print("a en b zijn even veel waard")
else:
  
  print("a is greater than b")
  max = a
  min = b

  print("het minimum is ", b, " en het maximum is", a)
  