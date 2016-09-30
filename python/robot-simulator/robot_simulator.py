#A robot factory's test facility needs a program to verify robot movements.
#
#The robots have three possible movements:
#
#- turn right
#- turn left
#- advance
#
#Robots are placed on a hypothetical infinite grid, facing a particular
#direction (north, east, south, or west) at a set of {x,y} coordinates,
#e.g., {3,8}, with coordinates increasing to the north and east.
#
#The robot then receives a number of instructions, at which point the
#testing facility verifies the robot's new position, and in which
#direction it is pointing.
#
#- The letter-string "RAALAL" means:
#  - Turn right
#  - Advance twice
#  - Turn left
#  - Advance once
#  - Turn left yet again
#- Say a robot starts at {7, 3} facing north. Then running this stream
#  of instructions should leave it at {9, 4} facing west.

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

class Robot:
    def __init__(self,bearing=NORTH,x=0,y=0):
        if bearing not in [NORTH, EAST, SOUTH, WEST]:
            raise ValueError('Invalid Bearing: Bearing must be NORTH, SOUTH, EAST, or WEST')
        self.bearing = bearing
        self.coordinates = (x, y)

    def _set_coords(self,dx=0,dy=0):
        self.coordinates = (self.coordinates[0]+dx, self.coordinates[1]+dy)

    def turn_right(self):
        self.bearing = (self.bearing + 1)%4

    def turn_left(self):
        self.bearing = (self.bearing - 1)%4

    def advance(self):
        if self.bearing == NORTH:
            self._set_coords(dy=1)
        elif self.bearing == EAST:
            self._set_coords(dx=1)
        elif self.bearing == SOUTH:
            self._set_coords(dy=-1)
        else: #must be facing west
            self._set_coords(dx=-1)

    def simulate(self, cmds):
        if not all(cmd in 'RLA' for cmd in cmds):
            raise ValueError('Invalid Command String: All commands must be "L", "R", or "A"')
        for cmd in cmds:
            if cmd == 'L':
                self.turn_left()
            elif cmd == 'R':
                self.turn_right()
            elif cmd == 'A':
                self.advance()


    def __str__(self):
        return 'Bearing = {}, X = {}, Y = {}'.format(['NORTH','EAST','SOUTH','WEST'][self.bearing],self.coordinates[0],self.coordinates[1])
