from random import randint

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
    "attic": {"items": [], "directions": {"down": "hall"}},
    "basement": {"items": [], "directions": {"up": "hall"}},
    "king bed": {
        "items": [],
        "directions": {"right": "hall", "left": "pantry"},
    },
    "corridor": {
        "items": [],
        "directions": {"right": "kid's bed", "left": "hall"},
    },
    "kid's bed": {"items": [], "directions": {"left": "corridor"}},
    "pantry": {"items": [], "directions": {"right": "king bed"}},
}

monsters = ["killer", "Nagini"]
monster_room_list = ["king bed", "pantry", "corridor", "kid's bed"]
all_items = ["sword", "gun", "key", "debbie"]
item_room_list = ["attic", "pantry", "basement", "kid's bed"]

is_p_in_maze = True


def assign_monster(rooms, monster_room_list, monsters):
    for i in range(len(monsters)):
        m_room_index = randint(0, len(monster_room_list) - 1)
        m_room = monster_room_list[m_room_index]
        rooms[m_room]["items"].append(monsters[i])


def assign_items(rooms, item_room_list, all_items):
    for i in range(len(all_items) - 1, -1, -1):
        i_room_index = randint(0, len(item_room_list) - 1)
        i_room = item_room_list[i_room_index]
        rooms[i_room]["items"].append(all_items[i])
        all_items.remove(all_items[i])
        item_room_list.remove(i_room)


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


def check_for_monsters(current_room, rooms, inventory):
    global is_p_in_maze
    if "killer" in rooms[current_room]["items"] and "gun" not in inventory:
        is_p_in_maze = False
        print("The Monster got you! YOU LOSE!!!!")
    elif "killer" in rooms[current_room]["items"] and "gun" in inventory:
        print("You killed the killer! Yay!!!")
        rooms[current_room]["items"].remove("killer")
    if "Nagini" in rooms[current_room]["items"] and "sword" not in inventory:
        is_p_in_maze = False
        print("Nagini got you! YOU LOSE!!!!")
    elif "Nagini" in rooms[current_room]["items"] and "sword" in inventory:
        print("You killed Nagini! Yay!!!")
        rooms[current_room]["items"].remove("Nagini")


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
            pick_up_available = False
    print("Your inventory: ", inventory)


def check_if_won(current_room, inventory):
    global is_p_in_maze
    if current_room == "basement" and "key" in inventory and "debbie" in inventory:
        print("O_O You won... YOU ARE AMAZING, YOU WIN!!!!! O_O")
        is_p_in_maze = False


def assign(rooms, monster_room_list, monsters, item_room_list, all_items):
    assign_monster(rooms, monster_room_list, monsters)
    assign_items(rooms, item_room_list, all_items)


current_room = "hall"
inventory = []

assign(rooms, monster_room_list, monsters, item_room_list, all_items)

while is_p_in_maze:
    current_room = ask_for_room(current_room, rooms)
    check_for_monsters(current_room, rooms, inventory)
    if is_p_in_maze == False:
        break
    ask_for_items(current_room, inventory, rooms)
    check_if_won(current_room, inventory)
    if is_p_in_maze == False:
        break
    is_p_in_maze = True
