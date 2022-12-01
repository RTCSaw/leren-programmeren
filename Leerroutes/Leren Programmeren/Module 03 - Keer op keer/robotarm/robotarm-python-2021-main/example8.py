from RobotArm import RobotArm
robotArm = RobotArm('exercise 8')
robotArm.moveRight()
for x in range(7):
    robotArm.grab()
    for y in range(8):
        robotArm.moveRight()
    robotArm.drop()
    for z in range(8):
        robotArm.moveLeft()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()