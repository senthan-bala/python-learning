import numbers

file_1 = open("games/files/menu.txt", "r")
txt = file_1.read()
lines = txt.splitlines()


def convertToNumber(str):
    try:
        return int(str)
    except ValueError:
        try:
            return float(str)
        except ValueError:
            return str


def file_reader(lines):
    items = []
    for line in lines:
        item = {}
        thing, price, amt = line.split(" - ")
        item["thing"] = thing
        item["price"] = float(price)
        item["amount"] = int(amt)
        items.append(item)
    return items


def check_if_valid(what_customer_wants, items):
    is_thing_valid = False
    for item in items:
        if what_customer_wants == item["thing"]:
            is_thing_valid = True
    if is_thing_valid == False:
        print("Sorry! That's not an item on the menu! Please try again!")

    return is_thing_valid


def ask_for_items(items):
    print("Pick what you want from this:", "\n")
    for item in items:
        print(item)
    customer_items = []
    should_it_keep_going = True
    print("\n", "If you are done please press enter.")
    while should_it_keep_going:
        what_customer_wants = input("\n" + "Which ones would you like? ")
        what_customer_wants = what_customer_wants.title()
        if what_customer_wants == "":
            print("OK, Thank you for buying at the Indian shop!, Come back soon!")
            break
        is_thing_valid = check_if_valid(what_customer_wants, items)
        if is_thing_valid == True:
            customer_items.append(what_customer_wants)
    return customer_items


def amt_finder(customer_items, items):
    item_amounts=[]
    for item in items:
        item_amount = {}
        item_amount["amount"] = 0
        for customer_item in customer_items:
            if customer_item == item["thing"]:
                item_amount["thing"] = customer_item
                item_amount["amount"] = int(item_amount["amount"]) + 1
        item_amounts.append(item_amount)
    return item_amounts
                

def amt_changer(item_amounts):
    for item_amount in item_amounts:
        item_amt_holder={}
       


def price_finder(customer_items, items):
    prices = []
    for item in items:
        for customer_item in customer_items:
            if customer_item == item["thing"]:
                prices.append(item["price"])
    prices.append(0)
    return prices


def finalize_price(prices):
    final_price = 0
    for price in prices:
        final_price = final_price + price
    return final_price


def ask_for_price(final_price):
    is_price_paid = False
    print("This is the price you have to pay: $", final_price)
    while is_price_paid == False:
        pay_type = input("How would you like to pay: cash or credit ")
        pay_type = pay_type.title()
        if pay_type == "Credit":
            print("Ok, price paid!")
            is_price_paid = True
            break
        elif pay_type == "Cash":
            is_cash_paid = False
            while is_cash_paid == False:
                cash_amount = input("How much will you pay? ")
                cash_amount = convertToNumber(cash_amount)
                if isinstance(cash_amount, numbers.Number):
                    cash_amount = int(cash_amount)
                    if cash_amount >= final_price:
                        change = cash_amount - final_price
                        change = round(change, 2)
                        print("Here is your change:", change)
                        is_price_paid = True
                        break
                    elif cash_amount < final_price:
                        print("Sorry, that's not enough, please try again!")
                else:
                    print("Sorry, you can't pay like that, please try again!")

        else:
            print("Sorry, you can't pay like that, please try again!")


def command(lines):
    items = file_reader(lines)
    customer_items = ask_for_items(items)
    item_amounts = amt_finder(customer_items,items)
    prices = price_finder(customer_items, items)
    final_price = finalize_price(prices)
    ask_for_price(final_price)


command(lines)
