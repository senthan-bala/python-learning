import math

numbers = [17, 25, 13, 33, 29, 28, 47, 121]


def find_prime_num(number):
    is_prime=True
    sqrt_num= int(math.sqrt(number))
    for divisor in range(2, sqrt_num+1):
        remainder = number % divisor
        if remainder == 0:
            is_prime = False
            factor=divisor
            break
        elif remainder != 0:
            factor=0
    if is_prime == False:
        print(number, " is not a prime number, it is divisible by ", factor)
    elif is_prime == True:
        print(number, " is a prime number")    


for number in numbers:
    find_prime_num(number)