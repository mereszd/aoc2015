all_guests = []
guest_connections = []
full_seats = []


def calculate_chain(current_guest, guests, seated, total_happiness):
    print(f"Currently at {current_guest}, can go to {guests}")
    print(f"Total happiness is at {total_happiness}")
    seated.append(current_guest)
    print(f"Seated guests are now {seated}")
    if len(guests) == 0:
        print(f"Everybody is seated now. Calculating the last happiness between last ({seated[-1]}) and first ({seated[0]}) guest.")
        for guest_connection in guest_connections:
            if guest_connection[0] == seated[-1] and guest_connection[2] == seated[0]:
                print(f"Adding {guest_connection[1]} due to {guest_connection[0]} and {guest_connection[2]}.")
                total_happiness += guest_connection[1]
            if guest_connection[2] == seated[-1] and guest_connection[0] == seated[0]:
                print(f"Adding {guest_connection[1]} due to {guest_connection[0]} and {guest_connection[2]}.")
                total_happiness += guest_connection[1]
        full_seats.append([seated, total_happiness])
        return True
    for guest in guests:
        print(f"{guest} is available, checking it now")
        happiness_addition = 0
        for guest_connection in guest_connections:
            if guest_connection[2] == current_guest and guest_connection[0] == guest:
                happiness_addition += guest_connection[1]
                print(f"Adding {guest_connection[1]} due to {guest_connection[0]} and {guest_connection[2]}.")
                print(f"Happiness addition is at {happiness_addition}")
            if guest_connection[0] == current_guest and guest_connection[2] == guest:
                happiness_addition += guest_connection[1]
                print(f"Adding {guest_connection[1]} due to {guest_connection[0]} and {guest_connection[2]}.")
                print(f"Happiness addition is at {happiness_addition}")
        print(f"{guest} is the next seated guest")
        new_inner_guests = guests.copy()
        new_inner_guests.remove(guest)
        calculate_chain(guest, new_inner_guests, seated.copy(), total_happiness + happiness_addition)


with open('13_input.txt', 'r') as file:
    contents = file.readlines()
    lines = [line.strip() for line in contents]
    for line in lines:
        guest_1, _, effect_type, effect, _, _, _, _, _, _, guest_2 = line.split()
        if guest_1 not in all_guests:
            all_guests.append(guest_1)
        if effect_type == 'gain':
            guest_connections.append([guest_1, int(effect), guest_2[:-1]])
        else:
            guest_connections.append([guest_1, int(effect) * -1, guest_2[:-1]])
    all_guests.append('Myself')
    for g in all_guests:
        guest_connections.append([g, 0, 'Myself'])
        guest_connections.append(['Myself', 0, g])

for g in all_guests:
    new_guests = all_guests.copy()
    new_guests.remove(g)
    calculate_chain(g, new_guests, [], 0)


best_seating = None
max_happiness = None
for full_seat in full_seats:
    if max_happiness is None:
        max_happiness = full_seat[1]
        best_seating = full_seat[0]
    elif max_happiness < full_seat[1]:
        max_happiness = full_seat[1]
        best_seating = full_seat[0]
    print(f"{full_seat[0]}, {full_seat[1]}")

print(f"Best seating is {best_seating}, maximum happiness is {max_happiness}")