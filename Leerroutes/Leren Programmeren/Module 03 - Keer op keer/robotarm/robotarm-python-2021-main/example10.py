from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')
robotArm.speed = 2
x = 9
c = 8
for y in range(5):
    robotArm.grab()
    for y in range(x):
        robotArm.moveRight()
    robotArm.drop()
    for y in range (c):
        robotArm.moveLeft()
    x-=2
    c-=2 

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()