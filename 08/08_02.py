with open('08_input.txt', 'r') as file:
    contents = file.readlines()
    lines = [line.strip() for line in contents]
    totalString = 0
    totalEncoded = 0
    for line in lines:
        print(f"Calculating {line}")
        totalString += len(line)
        newline = "\""
        for char in line:
            print(f"Calculating {char}")
            if char == '\"':
                newline += '\\\"'
            elif char == '\\':
                newline += '\\\\'
            else:
                newline += char
        newline += "\""
        totalEncoded += len(newline)
        print(f"Line is {line}, length is {len(line)}. Newline is {newline}, length is {len(newline)}")


    print(f"Total String is {totalString}, Total Encoded is {totalEncoded} so the result is {totalEncoded-totalString}")