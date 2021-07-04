def read_file():
    file_1 = open("games/files/bank.txt", "r")
    txt = file_1.read()
    lines = txt.splitlines()
    file_1.close()
    return lines


def place_items(lines):
    accounts = []
    for line in lines:
        account = {}
        name, amt, password = line.split(",")
        account["name"] = name
        account["amt"] = int(amt)
        account["pass"] = int(password)
        accounts.append(account)
    return accounts


def write_file(accounts):
    file_1 = open("games/files/bankYeet.txt", "w")
    rep_lines = []
    for account in accounts:
        rep_line = ",".join(
            [account["name"], str(account["amt"]), str(account["pass"])]
        )
        rep_lines.append(rep_line)
    line = "\n".join(rep_lines)
    file_1.write(line)
    file_1.close()
    return rep_lines


def is_pass_val(accounts):
    is_password_val = False
    while not is_password_val:
        pass_ = input("What is your password?")
        if pass_.isdigit() == True:
            for account in accounts:
                if int(pass_) == account["pass"]:
                    is_password_val = True
                    break
        if is_password_val == False:
            print("Sorry thats not a valid password! Try again!")
    return int(pass_)


def ask_for_person(accounts, pass_):
    is_person_val = False
    is_amt_val = False
    while not is_person_val:
        person = input("Who would you like to transfer money to?")
        person = person.strip()
        for account in accounts:
            if account["name"] == person:
                if account["pass"] == pass_:
                    print("You cant transfer money to yourself.")
                else:
                    is_person_val = True
        if is_person_val == False:
            print("Sorry, that is not a valid input.")
    return is_amt_val, person


def ask_for_transfer_amt(accounts, is_amt_val, pass_, person):
    while not is_amt_val:
        trans_amt = input("How much would you like to transfer?")
        trans_amt = trans_amt.strip()
        if trans_amt.isdigit() == True:
            trans_amt = int(trans_amt)
            is_amt_val = True
            for account in accounts:
                sender = account["name"]
                sender_amt = account["amt"]
                if account["pass"] == pass_:
                    break
            for account in accounts:
                taker = account["name"]
                taker_amt = account["amt"]
                if person == taker:
                    break
            sender_amt = sender_amt - trans_amt
            taker_amt = taker_amt + trans_amt
            for account in accounts:
                if account["name"] == sender:
                    account["amt"] = sender_amt
                elif account["name"] == taker:
                    account["amt"] = taker_amt
            print(taker_amt, sender_amt)

        else:
            print("Sorry thats not a valid amt")


def withdraw(accounts, pass_):
    wd_amt = input("How much would you like to withdraw?")
    if wd_amt.isdigit() == True:
        wd_amt = int(wd_amt)
        for account in accounts:
            if int(account["pass"]) == pass_:
                account["amt"] = account["amt"] - wd_amt
                print("New amt:", account["amt"])
                break
    else:
        print("Sorry thats not a valid amount! Try again!")


def deposit(accounts, pass_):
    dep_amt = input("How much would you like to deposit?")
    dep_amt = dep_amt.strip()
    if dep_amt.isdigit() == True:
        dep_amt = int(dep_amt)
        for account in accounts:
            if int(account["pass"]) == pass_:
                account["amt"] = account["amt"] + dep_amt
                print("New amt:", account["amt"])
                break
    else:
        print("Sorry thats not a valid amount! Try again!")


def ask_input(accounts, pass_):
    is_inp_val = False
    while not is_inp_val:
        inp = input("Would you like to Deposit, Withdraw, Transfer, or Check?")
        inp = inp.lower().strip()
        if inp == "deposit":
            deposit(accounts, pass_)
        elif inp == "withdraw":
            withdraw(accounts, pass_)
        elif inp == "transfer":
            is_amt_val, person = ask_for_person(accounts, pass_)
            ask_for_transfer_amt(accounts, is_amt_val, pass_, person)
        elif inp == "check":
            for account in accounts:
                if account["pass"] == pass_:
                    print("Here is your account balance:", account["amt"])
        elif inp == "":
            break
        else:
            print("Sorry thats not a valid option! Try again!")


def main():
    lines = read_file()
    accounts = place_items(lines)
    pass_ = is_pass_val(accounts)
    ask_input(accounts, pass_)
    write_file(accounts)


main()
