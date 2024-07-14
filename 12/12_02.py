import json
json_sum = 0


def iterate_json(obj):
    global json_sum
    if isinstance(obj, dict):
        ignore = False
        for value in obj.values():
            if isinstance(value, str) and value == "red":
                print(f"Ignoring {obj.items()} as red is in it.")
                ignore = True
                break
        if ignore is False:
            for key, value in obj.items():
                iterate_json(value)
    elif isinstance(obj, list):
        for item in obj:
            iterate_json(item)
    else:
        try:
            json_sum += int(obj)
        except ValueError:
            pass


with open('12_input.txt', 'r') as file:
    contents = file.read()
    iterate_json(json.loads(contents))
    print(json_sum)
