import random

liste_1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Robot:
    robot_list = []

    def __init__(self):
        self.name = self.generate_name()

        self.robot_list.append(self.name)

    def generate_name(self):
        while True:
            robot_name = []
            for i in range(2):
                robot_name.append(random.choices(liste_1))
            for j in range (3):
                robot_name.append(str(random.randint(0,9)))
            robot_name = "".join("".join(robot) for robot in robot_name)
            if robot_name not in self.robot_list:
                return robot_name

    def reset(self):
        self.name = self.generate_name()
        