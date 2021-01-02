import math

number_list = [53, 46, 67, 23, 2, 87]


def find_min(numbers):
    min_number = None

    for number in numbers:
        if min_number == None:
            min_number = number
        elif number <= min_number:
            min_number = number

    return min_number


def find_max(numbers):
    max_number = None

    for number in numbers:
        if max_number == None:
            max_number = number
        elif number >= max_number:
            max_number = number

    return max_number


def find_prime(number):
    is_prime = True
    sqrt_number = int(math.sqrt(number))
    for abc in range(2, sqrt_number + 1):
        remainder = number % abc
        if remainder == 0:
            print(number, "is not a prime; it is divisible by", abc)
            is_prime = False
            break

    if is_prime == True:
        print(number, "is a prime number")


for number in number_list:
    find_prime(number)

print("Smallest number : ", find_min(number_list))
print("Biggest number : ", find_max(number_list))

# print("Smallest number : ", min(number_list))
# print("Biggest number : ", max(number_list))


# a = 7443674
# b = 3

# rem_2 = a % b
# f_2= int((a- rem_2)/ b)
# print('Factor : ',f_2,',Remainder : ',rem_2,',Divisible : ',rem_2== 0)

