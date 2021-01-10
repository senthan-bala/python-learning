from random import choice


all_items = [
    "spider",
    "flashlight",
    "dementor",
    "sword",
    "assassin",
    "gun",
    "zombie",
    "chainsaw",
    "MONster",
    "key",
    "debbie",
    "gold",
]

rooms = {
    "a1": {"movements": {"right": "a2", "down": "b1"}, "items": []},
    "a2": {"movements": {"left": "a1", "right": "a3", "down": "b2"}, "items": []},
    "a3": {"movements": {"left": "a2", "right": "a4", "down": "b3"}, "items": []},
    "a4": {"movements": {"left": "a3", "down": "b4"}, "items": []},
    "b1": {"movements": {"up": "a1", "down": "c1", "right": "b2"}, "items": []},
    "b2": {
        "movements": {"up": "a2", "down": "c2", "left": "b1", "right": "b3"},
        "items": [],
    },
    "b3": {
        "movements": {"up": "a3", "down": "c3", "left": "b2", "right": "b4"},
        "items": [],
    },
    "b4": {"movements": {"up": "a4", "down": "c4", "left": "b3"}, "items": []},
    "c1": {"movements": {"up": "b1", "down": "d1", "right": "c2"}, "items": []},
    "c2": {
        "movements": {"up": "b2", "down": "d2", "left": "c1", "right": "c3"},
        "items": [],
    },
    "c3": {
        "movements": {"up": "b3", "down": "d3", "left": "c2", "right": "c4"},
        "items": [],
    },
    "c4": {"movements": {"up": "b4", "down": "d4", "left": "c3"}, "items": []},
    "d1": {"movements": {"right": "d2", "up": "c1"}, "items": []},
    "d2": {"movements": {"left": "d1", "right": "d3", "up": "c2"}, "items": []},
    "d3": {"movements": {"left": "d2", "right": "d4", "up": "c3"}, "items": []},
    "d4": {"movements": {"left": "d3", "up": "c4"}, "items": []},
}


def place_items():
    for item in all_items:
        room_name = choice(list(rooms.keys()))
        rooms[room_name]["items"].append(item)


def look_for_monster():
    got_killed = False
    if "spider" in current_room["items"] and "flashlight" in backpack:
        print("You killed a giant spider!")
        current_room["items"].remove("spider")
        backpack.remove("flashlight")
    elif "spider" in current_room["items"] and "flashlight" not in backpack:
        print("You got killed by a giant spider!!! You lose")
        got_killed = True
    if "zombie" in current_room["items"] and "chainsaw" in backpack:
        print("You killed a zombie!")
        current_room["items"].remove("zombie")
        backpack.remove("chainsaw")
    elif "zombie" in current_room["items"] and "chainsaw" not in backpack:
        print("You got killed by a zombie!!! You lose")
        got_killed = True
    if "dementor" in current_room["items"] and "sword" in backpack:
        print("You killed a dementor!")
        current_room["items"].remove("dementor")
        backpack.remove("sword")
    elif "dementor" in current_room["items"] and "sword" not in backpack:
        print("You got killed by a dementor!!! You lose")
        got_killed = True
    if "assassin" in current_room["items"] and "gun" in backpack:
        print("You killed an assassin!")
        current_room["items"].remove("assassin")
        backpack.remove("gun")
    elif "assassin" in current_room["items"] and "gun" not in backpack:
        print("You got killed by an assassin!!! You lose")
        got_killed = True
    if "MONster" in current_room["items"]:
        print("You got killed by MONster!!! You lose!!!")
        current_room["items"].remove("MONster")
        got_killed = True
    return got_killed


current_room = rooms["a1"]
in_the_maze = True
backpack = []

place_items()

while in_the_maze:
    got_killed = look_for_monster()
    if got_killed == True:
        break
    while current_room["items"] != []:
        get = input("Items available - " + str(current_room["items"]) + " : ")
        if get == "":
            break
        elif get not in current_room["items"]:
            print("That is not an item")
            continue
        elif get in current_room["items"]:
            current_room["items"].remove(get)
            backpack.append(get)
    go = input(str(list(current_room["movements"].keys())) + " : ")
    if go not in current_room["movements"]:
        print("oops! you have to type the right word")
        continue
    next_room = current_room["movements"][go]
    current_room = rooms[next_room]
    print("You are in", next_room, ", Backpack =>", backpack)
    if next_room == "d4":
        in_the_maze = False
        print("Yaaaaay!!! You win!!!! You saved debbie!!!!!")
