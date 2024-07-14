def enough_vowels(test_string):
    n = 0
    for char in test_string:
        if char in "aeiou":
            n += 1
    return True if n >= 3 else False


def repeating_chars(test_string):
    for index, char in enumerate(test_string):
        if index == 0:
            pass
        elif test_string[index] == test_string[index-1]:
            return True
    return False


def not_containing(test_string):
    for badstring in ["ab", "cd", "pq", "xy"]:
        if badstring in test_string:
            return False
    return True


def test(test_string):
    if enough_vowels(test_string) and repeating_chars(test_string) and not_containing(test_string):
        return True
    return False

with open('05_input.txt', 'r') as file:
    contents = file.readlines()
    sum = 0
    lines = [line.strip() for line in contents]
    for line in lines:
        if test(line):
            sum += 1
    print(sum)