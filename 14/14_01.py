reindeers = []
reindeer_times = []


def calculate_distance (reindeer, total_time):
    status = "flying"
    time = reindeer[2]
    distance = 0
    for i in range(1, total_time+1):
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
    print(f"{reindeer[0]} has traveled {distance} km after {total_time} seconds.")
    reindeer_times.append([reindeer[0], distance])
    return True


with open('14_input.txt', 'r') as file:
    contents = file.readlines()
    lines = [line.strip() for line in contents]
    for line in lines:
        name, _, _, speed, _, _, flyingTime, _, _, _, _, _, _, restTime, _ = line.split()
        reindeers.append([name, int(speed), int(flyingTime), int(restTime)])
    for r in reindeers:
        calculate_distance(r, 2503)

maxDistance = None
bestReindeer = None
for r_t in reindeer_times:
    if maxDistance is None:
        bestReindeer = r_t[0]
        maxDistance = r_t[1]
    elif maxDistance < r_t[1]:
        bestReindeer = r_t[0]
        maxDistance = r_t[1]

print(f"The best reindeer is {bestReindeer} with distance {maxDistance}")