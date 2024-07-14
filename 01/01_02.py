with open('01_input.txt', 'r') as file:
    contents = file.read()
    floor = 0
    for index, char in enumerate(contents):
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        if floor < 0:
            print(index+1)
            break