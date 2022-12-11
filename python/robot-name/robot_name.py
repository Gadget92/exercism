import string
import random


class Robot(object):
    robot_names = []

    def __init__(self):
        self.name = self.get_valid_name()

    def reset(self):
        self.name = self.get_valid_name()

    def get_valid_name(self):
        robot_name = ''
        while True:
            robot_name = self.get_name()
            if robot_name not in self.robot_names:
               self.robot_names.append(robot_name) 
               break
        return robot_name

    def get_name(self, char_length=2, number_length=3):
        res = ''.join(random.choice(string.ascii_uppercase) for i in range(char_length)) + \
               ''.join(random.choice(string.digits) for i in range(number_length))
        return res

