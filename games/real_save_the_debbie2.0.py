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
        "items": ["monster"],
        "directions": {"right": "kid's bed", "left": "hall"},
    },
    "kid's bed": {"items": ["debbie"], "directions": {"left": "corridor"}},
}

is_p_in_maze = True


def ask_for_room(current_room, rooms):
    directions = str(list(rooms[current_room]["directions"]))
    is_direction_valid = False
    while not is_direction_valid:
        print(
            "Directions available: ", str(list(rooms[current_room]["directions"])), ": "
        )
        next_room_direction = input()
        next_room_direction = next_room_direction.strip()
        for direction in list(rooms[current_room]["directions"]):
            if next_room_direction == direction:
                is_direction_valid = True
                break
        if is_direction_valid == False:
            print("Sorry that's not a valid direction, try again!")
    current_room = change_room(current_room, next_room_direction)
    return current_room


def change_room(current_room, next_room_direction):
    current_room = rooms[current_room]["directions"][next_room_direction]
    return current_room


def check_for_monster(current_room, rooms, inventory):
    global is_p_in_maze
    if "monster" in rooms[current_room]["items"] and "gun" not in inventory:
        is_p_in_maze = False
        print("The Monster got you! YOU LOSE!!!!")
    elif "monster" in rooms[current_room]["items"] and "gun" in inventory:
        print("You killed the monster! Yay!!!")
        rooms[current_room]["items"].remove("monster")


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


def check_if_won(current_room, inventory):
    global is_p_in_maze
    if current_room == "basement" and "key" in inventory and "debbie" in inventory:
        print("O_O You won... YOU ARE AMAZING, YOU WIN!!!!! O_O")
        is_p_in_maze = False


current_room = "hall"
inventory = []

while is_p_in_maze:
    current_room = ask_for_room(current_room, rooms)
    check_for_monster(current_room, rooms, inventory)
    if is_p_in_maze == False:
        break
    ask_for_items(current_room, inventory, rooms)
    check_if_won(current_room, inventory)
    if is_p_in_maze == False:
        break
    is_p_in_maze = True
