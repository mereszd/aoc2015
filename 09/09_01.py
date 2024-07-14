all_locations = []
connections = []
complete_routes = []

def calculate_route (location, locations, visited, total_distance):
    print(f"Currently at {location}, can go to {locations}")
    visited.append(location)
    print(f"Visited is now {visited}")
    if len(locations) == 0:
        print(f"No more locations to visit. Route is {visited}, total distance is {total_distance}")
        complete_routes.append([visited, total_distance])
        return True
    for new_location in locations:
        print(f"{new_location} is available, testing if it has a route from {location}")
        for connection in connections:
            if new_location in connection and location in connection:
                print(f"{connection} is a valid location, moving there")
                new_inner_locations = locations.copy()
                new_inner_locations.remove(new_location)
                calculate_route(new_location, new_inner_locations, visited.copy(), total_distance+connection[2])


with open('09_input.txt', 'r') as file:
    contents = file.readlines()
    lines = [line.strip() for line in contents]
    for line in lines:
        location_1, _, location_2, _, distance = line.split()
        if location_1 not in all_locations:
            all_locations.append(location_1)
        if location_2 not in all_locations:
            all_locations.append(location_2)
        connections.append([location_1, location_2, int(distance)])

for loc in all_locations:
    new_locations = all_locations.copy()
    new_locations.remove(loc)
    calculate_route(loc, new_locations, [], 0)

min_distance = None
min_route = None
for route in complete_routes:
    if min_distance is None:
        min_distance = route[1]
        min_route = route[0]
    elif min_distance > route[1]:
        min_distance = route[1]
        min_route = route[0]
print(min_route)
print(min_distance)