starter = "3113322113"
iterations = [starter]

for i in range(51):
    result = ""
    for index, char in enumerate(iterations[i]):
        if index == 0:
            current_char = char
            current_seq = 1
        else:
            if char == current_char:
                current_seq += 1
            else:
                result += str(current_seq) + str(current_char)
                current_char = char
                current_seq = 1
    result += str(current_seq) + str(current_char)
    iterations.append(result)

print(len(iterations[50]))