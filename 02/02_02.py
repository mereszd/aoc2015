with open('02_input.txt', 'r') as file:
    contents = file.readlines()
    lines = [line.strip() for line in contents]
    sum = 0
    for line in lines:
        dimensions = line.split('x')
        dimensions = [int(char) for char in dimensions]
        dimensions.sort()
        sum += 2 * dimensions[0] + 2 * dimensions[1] + dimensions[0] * dimensions[1] * dimensions[2]
    print(sum)