from RobotArm import RobotArm
robotArm = RobotArm('exercise 7')
robotArm.moveRight()
robotArm.speed = 2
for r in range(5):
    for x in range(6):
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
        robotArm.moveRight()
    for y in range(2):
        robotArm.moveRight()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()