high_range = 101
low_range = 0
is_guess_correct = False

current_guess = int(((high_range - low_range) / 2) + low_range)

print("Pick a number between", low_range + 1, "and", high_range - 1)

while is_guess_correct == False:
    high_low = input("Is it " + str(current_guess) + "? H, L, or E: ")
    if high_low == "E":
        print("Yaay! I found the number!!!")
        is_guess_correct = True
    elif high_low == "H":
        low_range = current_guess
        current_guess = int(current_guess + (((high_range - current_guess) / 2) + 0.5))
    elif high_low == "L":
        high_range = current_guess
        current_guess = int(current_guess - (((current_guess - low_range) / 2) - 0.5))

