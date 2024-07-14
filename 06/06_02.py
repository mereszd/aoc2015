# Setting up the board
grid = []
for X in range(1000):
    line = []
    for Y in range(1000):
        line.append([X, Y, 0])
    grid.append(line)


def turn(start, end, state):
    sx, sy = start.split(',')
    ex, ey = end.split(',')
    for x in range(int(sx), int(ex)+1):
        for y in range(int(sy), int(ey)+1):
            if state == 'toggle':
                grid[x][y][2] += 2
            elif state == 'on':
                grid[x][y][2] += 1
            elif state == 'off':
                grid[x][y][2] -= 1
                if grid[x][y][2] < 0:
                    grid[x][y][2] = 0



with open('06_input.txt', 'r') as file:
    contents = file.readlines()
    sum = 0
    lines = [line.strip() for line in contents]
    for line in lines:
        if "turn on" in line:
            turn(line.split()[2], line.split()[4], "on")
        elif "turn off" in line:
            turn(line.split()[2], line.split()[4], "off")
        elif "toggle" in line:
            turn(line.split()[1], line.split()[3], "toggle")

    for row in grid:
        for light in row:
            sum += light[2]

    print(sum)