max_num = 101


def remove_mult(input_nums: list, multiple: int):
    output_nums = []
    for number in input_nums:
        remainder = number % multiple
        if remainder != 0:
            output_nums.append(number)
    return output_nums


def remove_no_mult(input_nums: list, multiple: int):
    output_nums = []
    for number in input_nums:
        remainder = number % multiple
        if remainder == 0:
            output_nums.append(number)
    return output_nums


numbers = []
for i in range(1, max_num):
    numbers.append(i)

print("Pick a number between 1 and", max_num - 1)

is_div_2 = input("Is it divisible by 2? ")
if is_div_2 == "Y":
    numbers = remove_no_mult(numbers, 2)
else:
    numbers = remove_mult(numbers, 2)

is_div_3 = input("Is it divisible by 3? ")
if is_div_3 == "Y":
    numbers = remove_no_mult(numbers, 3)
else:
    numbers = remove_mult(numbers, 3)

if is_div_2 == "Y":
    is_div_4 = input("Is it divisible by 4? ")
    if is_div_4 == "Y":
        numbers = remove_no_mult(numbers, 4)
    else:
        numbers = remove_mult(numbers, 4)


is_div_5 = input("Is it divisible by 5? ")
if is_div_5 == "Y":
    numbers = remove_no_mult(numbers, 5)
else:
    numbers = remove_mult(numbers, 5)

# print(numbers)
high_range = len(numbers)
low_range = -1

current_idx = int(((high_range - low_range) / 2) + low_range)
is_guess_correct = False

while is_guess_correct == False:
    high_low = input("Is it " + str(numbers[current_idx]) + "? H, L, or E: ")
    if high_low == "E":
        print("Yaay! I found the number!!!")
        is_guess_correct = True
    elif high_low == "H":
        low_range = current_idx
        current_idx = int(current_idx + (((high_range - current_idx) / 2) + 0.5))
        if current_idx >= len(numbers):
            current_idx = len(numbers) - 1
    elif high_low == "L":
        high_range = current_idx
        current_idx = int(current_idx - (((current_idx - low_range) / 2) - 0.5))
        if current_idx < 0:
            current_idx = 0

