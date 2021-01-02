robot_file = open("games/files/robot.txt", "r")

robots = {}


for line in robot_file.read().splitlines():
    name, speed, strength, intel = line.split(",")
    robots[name] = (int(speed), int(strength), intel)

robot_file.close()

yes_or_no = input("Do you want to choose a robot? ")
while yes_or_no == "yes":
    robot = input("Choose a robot " + str(list(robots.keys())))
    if robot not in robots:
        print("Sorry! Wrong input!")
        continue
    else:
        (speed, strength, intel) = robots[robot]
        print(
            "\nName:",
            robot,
            "\nSpeed:",
            speed,
            "\nStrength:",
            strength,
            "\nIntel:",
            intel,
        )
    yes_or_no = input("Do you want to keep going? ")

