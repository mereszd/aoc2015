starter_password = "vzbxxyzz"
current_password_ascii = [ord(char) for char in starter_password]


def increment_password (password_ascii, index):
    if password_ascii[index] > 121:
        password_ascii[index] = 97
        password_ascii = increment_password(password_ascii, index-1)
        return password_ascii
    else:
        password_ascii[index] += 1
        return password_ascii


def ignored (current_password_ascii):
    ignored_letters = [ord('i'), ord('o'), ord('l')]
    for ignored_letter in ignored_letters:
        if ignored_letter in current_password_ascii:
            # print(f"Ignored test failed. {ignored_letter} is in {current_password_ascii}")
            return False
    return True


def straight_three (current_password_ascii):
    for i in range(len(current_password_ascii)):
        if i > 1:
            if current_password_ascii[i - 2] == current_password_ascii[i] - 2 and current_password_ascii[i - 1] == current_password_ascii[i] - 1:
                # print(f"Straight Three test is passed for {current_password_ascii}, "
                      # f"as {current_password_ascii[i-2]}, {current_password_ascii[i-1]} and "
                      # f"{current_password_ascii[i]} satisfies the criteria.")
                return True
    # print(f"Straight Three test is failed for {current_password_ascii}")
    return False


def double_pairs (current_password_ascii):
    found_pairs = 0
    skip = 0
    for i in range(len(current_password_ascii)):
        if i == 0:
            pass
        elif skip == 1:
            skip = 0
            pass
        else:
            if current_password_ascii[i] == current_password_ascii[i-1]:
                found_pairs += 1
                skip = 1
    if found_pairs > 1:
        # print(f"Double Pairs test is passed for {current_password_ascii}")
        return True
    else:
        # print(f"Double Pairs test is failed for {current_password_ascii}")
        return False


while True:
    current_password_ascii = increment_password(current_password_ascii, 7)
    current_password = ''.join(chr(value) for value in current_password_ascii)
    if ignored(current_password_ascii) and straight_three(current_password_ascii) and double_pairs(current_password_ascii):
        print(f"{current_password} satisfies all criterias, result found.")
        break