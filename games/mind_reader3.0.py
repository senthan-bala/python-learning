numbers = []
max_num = 101
is_guess_correct = False

for i in range(1, max_num):
    numbers.append(i)


def remove_no_mult(numbers: list, multiple: int):
    numbers2 = []
    for number in numbers:
        remaider = number % multiple
        if remaider == 0:
            numbers2.append(number)
    return numbers2


def remove_mult(numbers: list, multiple: int):
    numbers2 = []
    for number in numbers:
        remaider = number % multiple
        if remaider != 0:
            numbers2.append(number)
    return numbers2


print("Pick a number between 1 and", max_num - 1)

is_div_2 = input("Is it divisible by two?")
if is_div_2 == "yes":
    numbers = remove_no_mult(numbers, 2)
elif is_div_2 == "no":
    numbers = remove_mult(numbers, 2)

is_div_3 = input("Is it divisible by three?")
if is_div_3 == "yes":
    numbers = remove_no_mult(numbers, 3)
elif is_div_3 == "no":
    numbers = remove_mult(numbers, 3)

if is_div_2 == "yes":
    is_div_4 = input("Is it divisible by four?")
    if is_div_4 == "yes":
        numbers = remove_no_mult(numbers, 4)
    elif is_div_4 == "no":
        numbers = remove_mult(numbers, 4)

is_div_5 = input("Is it divisible by five?")
if is_div_5 == "yes":
    numbers = remove_no_mult(numbers, 5)
elif is_div_5 == "no":
    numbers = remove_mult(numbers, 5)

print(numbers)

high_range = (len(numbers)) - 1
low_range = -1


def calc_guess(high_range, low_range):
    new_guess = int(low_range + ((high_range - low_range) / 2) + 0.5)
    return new_guess


current_guess = calc_guess(high_range, low_range)

while is_guess_correct == False:
    high_low = input("Is it " + str(numbers[current_guess]) + "?:")
    if high_low == "yes":
        is_guess_correct = True
        print("I got it correct!")
    elif high_low == "low":
        high_range = current_guess
        current_guess = calc_guess(high_range, low_range)
    elif high_low == "high":
        low_range = current_guess
        current_guess = calc_guess(high_range, low_range)
