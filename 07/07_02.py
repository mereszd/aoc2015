connections = {}
two_input = ["AND", "OR", "RSHIFT", "LSHIFT"]


def calculate_value(key):
    print(f"Calculating {key}")
    if connections[key][3]:
        print(f"{key} is calculated. Value is {connections[key][4]}")
        return connections[key][4]
    else:
        try:
            input_1 = int(connections[key][0])
            print(f"{key} input_1 is an integer: {connections[key][0]}")
        except ValueError:
            print(f"Calculating input_1 {connections[key][0]}")
            input_1 = calculate_value(connections[key][0])
        if connections[key][2] == "ASSIGNMENT":
            connections[key][4] = input_1
            connections[key][3] = True
        elif connections[key][2] == "AND":
            try:
                input_2 = int(connections[key][1])
                print(f"{key} input_2 is an integer: {connections[key][1]}")
            except ValueError:
                print(f"Calculating input_2 {connections[key][1]}")
                input_2 = calculate_value(connections[key][1])
            connections[key][3] = True
            connections[key][4] = input_1 & input_2
        elif connections[key][2] == "OR":
            try:
                input_2 = int(connections[key][1])
                print(f"{key} input_2 is an integer: {connections[key][1]}")
            except ValueError:
                print(f"Calculating input_2 {connections[key][1]}")
                input_2 = calculate_value(connections[key][1])
            connections[key][3] = True
            connections[key][4] = input_1 | input_2
        elif connections[key][2] == "NOT":
            connections[key][3] = True
            connections[key][4] = ~input_1
        elif connections[key][2] == "LSHIFT":
            connections[key][3] = True
            connections[key][4] = input_1 << int(connections[key][1])
        elif connections[key][2] == "RSHIFT":
            connections[key][3] = True
            connections[key][4] = input_1 >> int(connections[key][1])
        if connections[key][4] < 0:
            connections[key][4] = 65536 + connections[key][4]
    return connections[key][4]


with open('07_input.txt', 'r') as file:
    contents = file.readlines()
    lines = [line.strip() for line in contents]
    for line in lines:
        operation, output = line.split('->')
        output = output.strip()
        # List structure: INPUT_1, INPUT_2, OPERATOR, RESULT_READY, CALCULATED_RESULT
        if "NOT" in operation:
            connections[output] = [operation.split()[1], "N/A", "NOT", False, 0]
        elif len(operation.split()) == 1:
            # Assignment
            try:
                connections[output] = [int(operation.split()[0]), "N/A", "ASSIGNMENT", True, int(operation.split()[0])]
            except ValueError:
                connections[output] = [operation.split()[0], "N/A", "ASSIGNMENT", False, 0]
        elif operation.split()[1] in two_input:
            connections[output] = [operation.split()[0], operation.split()[2], operation.split()[1], False, 0]
        connections['b'] = [956, "N/A", "ASSIGNMENT", True, 956]
    for key in connections.keys():
        calculate_value(key)
    print(connections['a'])