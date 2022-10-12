from winreg import REG_OPTION_BACKUP_RESTORE
from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')
# robotArm.moveLeft
# robotArm.moveRight
# robotArm.grab
# robotArm.drop

# Jouw python instructies zet je vanaf hier:
for x in range(5):
    robotArm.grab()
    for q in range(2):
        robotArm.moveRight()
    robotArm.drop()
    if x < 4:
        for q in range(2):
            robotArm.moveLeft()

for g in range(5):
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
    robotArm.moveRight()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()