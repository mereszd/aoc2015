with open('08_input.txt', 'r') as file:
    contents = file.readlines()
    lines = [line.strip() for line in contents]
    totalString = 0
    totalMemory = 0
    for line in lines:
        print(f"Calculating {line}")
        totalString += len(line)
        skip = 0
        for index, char in enumerate(line):
            print(f"Calculating {char}")
            if skip != 0:
                print(f"Need to skip counting, skip is at {skip}")
                skip -= 1
                continue
            if char == '\\':
                print(f"Char is \\")
                print(f"Next char is {line[index + 1]}")
                if line[index+1] == '\\' or line[index+1] == '"':
                    skip = 1
                elif line[index+1] == 'x':
                    skip = 3
                print(f"Skip is set to {skip}")
            totalMemory += 1
            print(f"Increased totalMemory, it is now at {totalMemory}")
        totalMemory -= 2
        print(f"Removed 2 from totalMemory, after {line} totalMemory is now at {totalMemory}")

    print(f"Total String is {totalString}, Total Memory is {totalMemory} so the result is {totalString-totalMemory}")