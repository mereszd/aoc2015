def two_repeating(test_string):
    for index, char in enumerate(test_string):
        if index == 0:
            pass
        else:
            twochar = test_string[index-1] + test_string[index]
            if twochar in test_string[:index-1] or twochar in test_string[index+1:]:
                print(f"{test_string} passed two_repeating because of {twochar}")
                return True
    print(f"{test_string} failed two_repeating")
    return False


def between_them(test_string):
    for index, char in enumerate(test_string):
        if index < 2:
            pass
        elif test_string[index] == test_string[index-2]:
            print(f"{test_string} passed between_them because of {test_string[index-2:index+1]}")
            return True
    print(f"{test_string} failed between_them")
    return False


def test(test_string):
    if two_repeating(test_string) and between_them(test_string):
        print(f"{test_string} passed overall")
        return True
    print(f"{test_string} failed overall")
    return False

with open('05_input.txt', 'r') as file:
    contents = file.readlines()
    sum = 0
    lines = [line.strip() for line in contents]
    for line in lines:
        if test(line):
            sum += 1
    print(sum)