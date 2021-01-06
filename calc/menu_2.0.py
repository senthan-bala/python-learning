def read_file():
    file_1 = open("games/files/menu.txt", "r")
    content = file_1.read()
    lines = content.splitlines()
    file_1.close()
    return lines


def write_file(lines):
    file_1 = open("games/files/menu.txt", "w")
    line = "\n".join(lines)
    file_1.write(line)
    file_1.close()


def build_string_from_menu_items(menu_items: list) -> list:
    lines = []
    for item in menu_items:
        line = " - ".join([item["item"], str(item["price"]), str(item["stock"])])
        lines.append(line)
    return lines


def bill(order_items: list, final_price: float) -> None:
    print_order(order_items, final_price)
    pay_type = ask_pay_type()

    if pay_type == "credit":
        print("Ok! Money paid!")
    elif pay_type == "cash":
        pay_amount = ask_pay_amount(final_price)
        print("Ok, your change is", pay_amount - final_price, "dollars.")


def build_menu_items_from_string(lines):
    menu_items = []
    for line in lines:
        menu_item = {}
        item, price, stock = line.split(" - ")
        menu_item["item"] = item
        menu_item["price"] = float(price)
        menu_item["stock"] = int(stock)
        menu_items.append(menu_item)
    return menu_items


def print_menu(items):
    print("Options:")
    for i in items:
        print(i["item"], "- Price:", i["price"], ", - Stock:", i["stock"])
    print("(If you want to pick nothing, then type nothing)")


def print_order(order_items, final_price):
    print("Your order is:")
    for order_item in order_items:
        print(order_item["item"], order_item["how_many"])
    print("The bill is", final_price)


def find_menu_item(menu_items, item_name):
    for menu_item in menu_items:
        if menu_item["item"].lower() == item_name:
            return menu_item
    return None


def ask_quantity(item_stock):
    quantity_is_valid = False
    while not quantity_is_valid:
        how_many = input("How many do you need?:")
        if not how_many.isdigit():
            print("Sorry, thats not a valid quantity")
            continue
        elif int(how_many) > item_stock:
            print("Sorry, we do not have that much. We only have", item_stock)
            continue
        else:
            quantity_is_valid = True
    return int(how_many)


def ask_pay_type():
    pay_type_valid = False
    while not pay_type_valid:
        pay_type = input("How would you like to pay, with credit or cash?:")
        pay_type = pay_type.strip().lower()
        if pay_type == "cash" or pay_type == "credit":
            pay_type_valid = True
        else:
            print("Sorry,thats not a valid way to pay!")
    return pay_type


def ask_pay_amount(final_price):
    pay_amount_valid = False
    while not pay_amount_valid:
        pay_amount = input("How much would you like to pay?")
        pay_amount = pay_amount.strip()
        if not pay_amount.isdigit():
            print("Sorry, thats not a valid amount")
            continue
        elif int(pay_amount) < final_price:
            print("Sorry! Thats not enough money! Pay again please.")
            continue
        else:
            pay_amount_valid = True
    return float(pay_amount)


def ask_order_item(menu_items):
    order_item_valid = False
    is_serving_done = False
    while not order_item_valid:
        item_name = input("What would you like to pick?:")
        item_name = item_name.strip().lower()
        if item_name == "nothing" or item_name == "":
            is_serving_done = True
            order_item_valid = True
            break
        menu_item = find_menu_item(menu_items, item_name)
        if menu_item == None:
            print("Sorry, thats not on the menu")
        elif menu_item["stock"] <= 0:
            print("Sorry, we're out of stock on that item")
        else:
            order_item_valid = True

    return is_serving_done, item_name


def get_order(menu_items):
    is_serving_done = False
    order_items = []
    final_price: float = 0

    print_menu(menu_items)

    while not is_serving_done:
        is_serving_done, item_name = ask_order_item(menu_items)
        if is_serving_done == True:
            print("\nAlright, we will get your order in a jiffy!")
            break

        menu_item = find_menu_item(menu_items, item_name)
        how_many = ask_quantity(menu_item["stock"])
        order_item = {}
        order_item["item"] = item_name
        order_item["how_many"] = int(how_many)
        order_items.append(order_item)
        final_price = finalize_price(menu_items, how_many, item_name, final_price)
        print("Added", item_name, "to the order!!")
    return order_items, final_price


def finalize_price(menu_items: list, how_many, item_name, final_price):
    menu_item = find_menu_item(menu_items, item_name)
    order_item_price = menu_item["price"] * how_many
    final_price = final_price + order_item_price
    revised_stock = menu_item["stock"] - how_many
    menu_item["stock"] = revised_stock
    return final_price


lines = read_file()
menu_items = build_menu_items_from_string(lines)
order_items, final_price = get_order(menu_items)
bill(order_items, final_price)
lines = build_string_from_menu_items(menu_items)
write_file(lines)
