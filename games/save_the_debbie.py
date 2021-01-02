rooms = {
    "hall": {
        "movements": {
            "up": "attic",
            "down": "basement",
            "right": "kitchen",
            "left": "pantry",
        },
        "items": [],
    },
    "pantry": {"movements": {"right": "hall"}, "items": ["gun"]},
    "kitchen": {
        "movements": {"left": "hall", "right": "kids room"},
        "items": ["Monsy Monsy"],
    },
    "kids room": {"movements": {"left": "kitchen"}, "items": ["debbie"]},
    "attic": {"movements": {"down": "hall"}, "items": ["key", "paper"]},
    "basement": {"movements": {"up": "hall"}, "items": []},
}

current_room = rooms["hall"]
in_the_maze = True
picked_up_items = []

def check_if_won(next_room_name, picked_up_items):
    global in_the_maze
    if (
        next_room_name == "basement"
        and "key" in picked_up_items
        and "debbie" in picked_up_items
    ):
        print("Hurray!!! You saved Debbie!!!! YOU WIN!!!!!")
        in_the_maze = False


def pickup_items():
    while current_room["items"] != []:
        item_msg = "Items : " + str(current_room["items"]) + " Anything to pick up? : "
        item = input(item_msg)
        if item == "":
            break
        else:
            if item not in current_room["items"]:
                print("Sorry, wrong input!!")
                continue
            else:
                picked_up_items.append(item)
                current_room["items"].remove(item)
                print("Basket =>", picked_up_items)


def move_to_room():
    global current_room
    directions = current_room["movements"].keys()
    while True:
        direction = input("Directions available : " + str(list(directions)) + " : ")
        if direction not in directions:
            print("Sorry, wrong input!!")
            continue
        else:
            break
    next_room_name = current_room["movements"][direction]
    current_room = rooms[next_room_name]
    print("Moved to", next_room_name, ", Basket => ", picked_up_items)
    return next_room_name


def check_for_monsy_monsy():
    global in_the_maze
    if "Monsy Monsy" in current_room["items"] and "gun" in picked_up_items:
        print("You killed the Monsy Monsy!!")
        current_room["items"].remove("Monsy Monsy")
    elif "Monsy Monsy" in current_room["items"] and "gun" not in picked_up_items:
        print("Monsy Monsy got you!! YOU LOOSE!!!")
        in_the_maze = False


print("You're stuck in Monsy Monsy's Maze!!!You have to save the Debbie!!!!")
while in_the_maze:
    pickup_items()
    next_room_name = move_to_room()
    check_for_monsy_monsy()
    check_if_won(next_room_name, picked_up_items)
