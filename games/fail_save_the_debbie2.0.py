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
    "kids room": {"movements": {"left": "kitchen"}, "items": ["debbie", "sword"]},
    "attic": {"movements": {"down": "hall"}, "items": ["key", "paper"]},
    "basement": {"movements": {"up": "hall"}, "items": ["The Dementor"]},
}

current_room = rooms["hall"]
in_the_maze = True
backpack = []

while in_the_maze:
    if "Monsy Monsy" in current_room["items"] and "gun" in backpack:
        print("Yaaay!!! You killed Monsy Monsy!!!")
        current_room["items"].remove("Monsy Monsy")
        current_room["items"].append("Monster horn")
    if "Monsy Monsy" in current_room["items"] and "gun" not in backpack:
        print("Monsy Monsy got you... YOU LOSE!!!!")
        break
    if "The Dementor" in current_room["items"] and "sword" in backpack:
        print("Yaaay!!! You killed The Dementor!!!")
        current_room["items"].remove("The Dementor")
        current_room["items"].append("Monster tooth")
    if "The Dementor" in current_room["items"] and "sword" not in backpack:
        print("The Dementor got you... YOU LOSE!!!!")
        break
    while current_room["items"] != []:
        get = input("This is what you can pick up:" + str(current_room["items"]))
        if get == "":
            break
        elif get not in current_room["items"]:
            print("That is not an item")
            continue
        elif get in current_room["items"]:
            current_room["items"].remove(get)
            backpack.append(get)
    print("Backpack =>", backpack)
    go = input(current_room["movements"].keys())
    if go not in current_room["movements"]:
        print("oops! you have to type the right word")
        continue
    next_room = current_room["movements"][go]
    current_room = rooms[next_room]
    print(next_room)
    if (
        next_room == "basement"
        and "debbie" in backpack
        and "key" in backpack
        and "Monster Tooth" in backpack
        and "Monster horn" in backpack
    ):
        in_the_maze = False
        print("Yaaaaay!!!You win!!!!You saved debbie!!!!!")
