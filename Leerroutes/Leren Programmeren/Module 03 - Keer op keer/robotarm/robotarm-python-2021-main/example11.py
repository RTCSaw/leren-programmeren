from string import whitespace
from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')
robotArm.speed = 2
q = 8
for x in range(q):
    robotArm.grab()
    color = robotArm.scan()
    if robotArm._color == "white":
        robotArm.moveRight()
        q -=2
        
    robotArm.drop()
    robotArm.moveRight()
    q-=2
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
