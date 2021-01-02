file_1 = open("games/files/menu.txt", "r")
txt = file_1.read()
lines = txt.splitlines()


def bill(order_items, final_price):
    print("Your order is:")
    for order_item in order_items:
        print(order_item["item"], order_item["how_many"])
    print("The bill is", final_price)
    pay_type = input("How would you like to pay, with credit or cash?:")
    if pay_type.lower() == "credit":
        print("Ok! Money paid!")
    elif pay_type.lower() == "cash":
        money = 0
        while money < final_price:
            money = input("How much would you like to pay?")
            money = float(money)
            if money >= final_price:
                print("Ok, your change is", money - final_price, "dollars.")
            elif money < final_price:
                print("Sorry! Thats not enough money! Pay again please.")
    else:
        print("Sorry,thats not a valid way to pay!")
        while pay_type.lower() != "credit" and pay_type.lower() != "cash":
            pay_type = input("How would you like to pay, with credit or cash?:")
            if pay_type.lower() == "credit":
                print("Ok! Money paid!")
            elif pay_type.lower() == "cash":
                money = 0
                while money < final_price:
                    money = input("How much would you like to pay?")
                    money = float(money)
                    if money >= final_price:
                        print("Ok, your change is", money - final_price, "dollars.")
                    elif money < final_price:
                        print("Sorry! Thats not enough money! Pay again please.")


def add_menu_items(lines):
    menu_items = []
    for line in lines:
        menu_item = {}
        item, price, stock = line.split(" - ")
        menu_item["item"] = item
        menu_item["price"] = float(price)
        menu_item["stock"] = int(stock)
        menu_items.append(menu_item)
    return menu_items


def check_if_valid(menu_items, chosen_item):
    is_serving_done = False
    valid = False
    for menu_item in menu_items:
        if chosen_item == menu_item["item"]:
            valid = True
            break
        elif chosen_item == "nothing" or chosen_item == "":
            is_serving_done = True
            break
    return valid, is_serving_done


def ask_for_input(menu_items):
    is_serving_done = False
    order_items = []
    final_price = 0

    print("Options:")
    for menu_item in menu_items:
        print(
            menu_item["item"],
            "- Price:",
            menu_item["price"],
            ", - Stock:",
            menu_item["stock"],
        )
    print("(If you want to pick nothing,then type ; nothing)")

    while not is_serving_done:
        item = input("\n" + "What would you like to pick?:")
        item = item.strip()
        valid, is_serving_done = check_if_valid(menu_items, item)

        if is_serving_done == True:
            print("\nAlright, we will get your order in a jiffy!")
            break

        if valid == True:
            how_many = input("How many do you need?:")
            if not how_many.isdigit():
                print("Sorry, thats not a valid quantity")
                continue
            for menu_item in menu_items:
                stock = menu_item["stock"]
                while int(how_many) > stock:
                    print("Sorry, we do not have that much.")
                    how_many = input("How many do you need?:")
                    if not how_many.isdigit():
                        print("Sorry, thats not a valid quantity")
                        continue
            order_item = {}
            order_item["item"] = item
            order_item["how_many"] = int(how_many)
            order_items.append(order_item)
            final_price, stock = finalize_price(menu_items, how_many, item, final_price)
            print("Added", item, "to the order!!")
        else:
            print("Sorry, thats not on the menu")
    return order_items, final_price


def finalize_price(menu_items: list, how_many, item, final_price):
    for menu_item in menu_items:
        stock = int(menu_item["stock"])
        if menu_item["item"] == item:
            price = float(menu_item["price"])
            price = price * int(how_many)
            final_price = final_price + price
            stock = stock - int(how_many)
            print(menu_item["item"], "Stock:", stock)
            menu_item["stock"] = stock
    return final_price, stock


menu_items = add_menu_items(lines)
order_items, final_price = ask_for_input(menu_items)
bill(order_items, final_price)

