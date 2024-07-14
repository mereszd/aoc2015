reindeers = []
reindeers_dict = {}
timelimit = 2503
reindeer_times = [[_, "N/A", 0] for _ in range(timelimit+1)]

def calculate_distance(reindeer):
    global timelimit
    status = "flying"
    time = reindeer[2]
    distance = 0
    for i in range(1, timelimit+1):
        if status == "flying":
            time -= 1
            distance += reindeer[1]
            print(f"Time is {i}, currently flying. Distance covered is {distance}, time left flying is {time}.")
            if time == 0:
                status = "resting"
                time = reindeer[3]
                print(f"Changing from flying to resting.")
        else:
            time -= 1
            print(f"Time is {i}, currently resting. Time left resting is {time}.")
            if time == 0:
                status = "flying"
                time = reindeer[2]
                print(f"Changing from resting to flying.")
        if reindeer_times[i][2] < distance:
            reindeer_times[i][1] = reindeer[0]
            reindeer_times[i][2] = distance
        elif reindeer_times[i][2] == distance:
            reindeer_times[i][1] += ',' + reindeer[0]
    print(f"{reindeer[0]} has traveled {distance} km after {timelimit} seconds.")
    return True


with open('14_input.txt', 'r') as file:
    contents = file.readlines()
    lines = [line.strip() for line in contents]
    for line in lines:
        name, _, _, speed, _, _, flyingTime, _, _, _, _, _, _, restTime, _ = line.split()
        reindeers.append([name, int(speed), int(flyingTime), int(restTime)])
    for r in reindeers:
        reindeers_dict[r[0]] = 0
        calculate_distance(r)

for rt in reindeer_times:
    if rt[1] == "N/A":
        pass
    elif ',' in rt[1]:
        multipleRd = rt[1].split(',')
        for mrd in multipleRd:
            reindeers_dict[mrd] += 1
    else:
        reindeers_dict[rt[1]] += 1

for key, value in reindeers_dict.items():
    print(key, value)

print(max(reindeers_dict.values()))