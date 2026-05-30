# CO3: Mobile Robot Localization using CSP

GRID_SIZE = 4

possible_positions = []

for x in range(GRID_SIZE):
    for y in range(GRID_SIZE):

        # Sensor Constraints
        near_wall = (x == 0 or y == 0)
        obstacle_detected = (x != 2)

        if near_wall and obstacle_detected:
            possible_positions.append((x, y))

print("Possible Robot Locations:")
for pos in possible_positions:
    print(pos)
