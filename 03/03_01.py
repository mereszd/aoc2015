with open('03_input.txt', 'r') as file:
    houses = []
    cX = 0
    cY = 0
    houses.append([cX, cY])
    print(houses)
    contents = file.read()
    for direction in contents:
        if direction == '^':
            cY += 1
        elif direction == 'v':
            cY -= 1
        elif direction == '<':
            cX -= 1
        elif direction == '>':
            cX += 1
        if [cX, cY] not in houses:
            print(f"{cX} {cY} not in houses, appending")
            houses.append([cX, cY])
        else:
            print(f"{cX} {cY} already visited")
    print(len(houses))