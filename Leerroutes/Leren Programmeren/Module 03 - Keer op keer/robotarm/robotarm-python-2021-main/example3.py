from RobotArm import RobotArm

robotArm = RobotArm('exercise 3')
# robotArm.moveLeft
# robotArm.moveRight
# robotArm.grab
# robotArm.drop

# Jouw python instructies zet je vanaf hier:
for x in range(4):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()

# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()