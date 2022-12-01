from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')
robotArm.speed = 3

x = 1

for y in range(0,4): #kolom
    for z in range(x):#per rij blokjes
        robotArm.grab()
        for y in range(0,5):#gaat 5 keer naar rechts
            robotArm.moveRight()
        robotArm.drop()#drop de blokjes
        for y in range(0,5):#gaat 5 keer naar links
            robotArm.moveLeft()
    robotArm.moveRight()#gaat nog een keer naar rechts
    x+=1   #telt na deze hele loop 1 bij de x op, zodat hij bij de volgende kolom 2 blokjes pakt etc. 
    
robotArm.wait()





# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()