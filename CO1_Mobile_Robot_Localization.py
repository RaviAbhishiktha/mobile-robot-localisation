# CO1: Mobile Robot Localization (State Representation)

from dataclasses import dataclass

@dataclass
class RobotState:
    x: int
    y: int
    direction: str

class MobileRobot:
    def __init__(self):
        self.state = RobotState(0, 0, "N")

    def move_forward(self):
        if self.state.direction == "N":
            self.state.y += 1
        elif self.state.direction == "S":
            self.state.y -= 1
        elif self.state.direction == "E":
            self.state.x += 1
        elif self.state.direction == "W":
            self.state.x -= 1

    def turn_left(self):
        directions = ["N", "W", "S", "E"]
        idx = directions.index(self.state.direction)
        self.state.direction = directions[(idx + 1) % 4]

    def turn_right(self):
        directions = ["N", "E", "S", "W"]
        idx = directions.index(self.state.direction)
        self.state.direction = directions[(idx + 1) % 4]

    def get_state(self):
        return self.state

# Test
robot = MobileRobot()

robot.move_forward()
robot.turn_right()
robot.move_forward()

print("Robot Location:")
print(robot.get_state())
