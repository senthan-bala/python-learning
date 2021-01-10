rooms = {
    "hall": {
        "items": [],
        "directions": {
            "up": "attic",
            "down": "basement",
            "right": "corridor",
            "left": "king bed",
        },
    },
    "attic": {"items": ["key"], "directions": {"down": "hall"}},
    "basement": {"items": [], "directions": {"up": "hall"}},
    "king bed": {"items": ["gun"], "directions": {"right": "hall"}},
    "corridor": {
        "items": ["Monster"],
        "directions": {"right": "kid's bed", "left": "hall"},
    },
    "kid's bed": {"items": ["debbie"], "directions": {"left": "corridor"}},
}

current_room = rooms["hall"]
is_p_in_maze = True
inventory = []


def ask_for_room(current_room):
    is_direction_valid = False
    while not is_direction_valid:
        next_room_direction = input(
            "Directions available: " + str(list(current_room["directions"])) + ": "
        )
        next_room_direction = next_room_direction.strip()
        for direction in list(current_room["directions"]):
            if next_room_direction == direction:
                is_direction_valid = True
                break
        if is_direction_valid == False:
            print("Sorry that's not a valid direction, try again!")
    current_room = change_room(current_room, next_room_direction)
    return current_room


def change_room(current_room, next_room_direction):
    current_room = current_room["directions"][next_room_direction]
    return current_room


def ask_for_items(current_room, inventory, rooms):
    items = rooms[current_room]["items"]
    pick_up_available = True
    while pick_up_available:
        if len(items) >= 1:
            print("Items available: ", items)
            pick_up_item = input("What would you like to pick up?: ")
            if pick_up_item in items:
                inventory.append(pick_up_item)
                items.remove(pick_up_item)
            elif pick_up_item == "":
                pick_up_available = False
            else:
                print("Sorry, that item is not in the room, try again.")
        else:
            print("There are no items in the room")
            pick_up_available = False
    print("Your inventory: ", inventory)


current_room = ask_for_room(current_room)
ask_for_items(current_room, inventory, rooms)
