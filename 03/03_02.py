with open('03_input.txt', 'r') as file:
    houses = [[0, 0]]
    coords = [[0, 0], [0, 0]]
    contents = file.read()
    movers = {'santa': 0, 'robosanta': 1}
    mover = 'santa'
    for direction in contents:
        if direction == '^':
            coords[movers[mover]][1] += 1
        elif direction == 'v':
            coords[movers[mover]][1] -= 1
        elif direction == '<':
            coords[movers[mover]][0] -= 1
        elif direction == '>':
            coords[movers[mover]][0] += 1

        if coords[movers[mover]] not in houses:
            print(f"{mover} is moving. His coordinates are {coords[movers[mover]][0]} {coords[movers[mover]][1]}, which is not in houses, appending")
            list_to_append = coords[movers[mover]].copy()
            houses.append(list_to_append)
            print(houses)
        else:
            print(f"{coords[movers[mover]][0]} {coords[movers[mover]][1]} already visited")

        if mover == 'santa':
            mover = 'robosanta'
        else:
            mover = 'santa'
    print(len(houses))
