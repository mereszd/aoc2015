with open('01_input.txt', 'r') as file:
    contents = file.read()
    floor = 0
    for c in contents:
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
    print(floor)