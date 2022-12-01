from RobotArm import RobotArm
robotArm = RobotArm()
robotArm.randomLevel(1,7)
count = 1
while count <9:
    robotArm.grab()
    color = robotArm.scan()
    if color == "":
        robotArm.wait()
    else:
        for i in range(count):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(count):
            robotArm.moveLeft()
        count += 1
robotArm.wait()