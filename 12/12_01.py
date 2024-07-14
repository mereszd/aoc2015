import json
json_sum = 0


def iterate_json(obj):
    global json_sum
    if isinstance(obj, dict):
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
