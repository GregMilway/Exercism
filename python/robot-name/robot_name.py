# create a robot class that generates a random name on instancing, and can be reset, which gets a new name.
# uses SystemRandom, for secure name generation

from random import SystemRandom
from string import ascii_uppercase, digits

used_names = []

class Robot:
    def __init__(self):
        self.rng = SystemRandom()
        self.reset()


    def reset(self):
        self.name = ''
        while self.name in used_names:
            self.name = ''.join(self.rng.choice(ascii_uppercase) for _ in range(2)) + \
            ''.join(self.rng.choice(digits) for _ in range(3))
        used_names.append(self.name)
