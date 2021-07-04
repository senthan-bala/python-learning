import numbers

equation = input("Please give an equation: ")
equation_lst = list(equation)
# equation_lst[0] = int(equation_lst[0])


def list_to_number(number):
    str_number = ""
    for digit in number:
        digit = str(digit)
        str_number += digit
    number = int(str_number)
    return number


def convertToNumber(str):
    try:
        return int(str)
    except ValueError:
        try:
            return float(str)
        except ValueError:
            return str


def find_question(equation_lst):
    has_operator_passed = False
    num1 = []
    num2 = []
    operator = ""
    for bit in equation_lst:
        if (
            bit == "0"
            or bit == "1"
            or bit == "2"
            or bit == "3"
            or bit == "4"
            or bit == "5"
            or bit == "6"
            or bit == "7"
            or bit == "8"
            or bit == "9"
        ):
            bit = int(bit)
        if operator != "" and isinstance(bit, numbers.Number):
            nothing = "blah"
        elif operator == "" and isinstance(bit, numbers.Number):
            nothing = "blah"
        elif operator == "" and isinstance(bit, numbers.Number) == False:
            has_operator_passed = True
            operator = bit
        else:
            break
        if isinstance(bit, numbers.Number) and has_operator_passed == False:
            num1.append(bit)
        elif isinstance(bit, numbers.Number) and has_operator_passed == True:
            num2.append(bit)
    return num1, operator, num2


def answer_question(num1, operator, num2):
    number1 = list_to_number(num1)
    number2 = list_to_number(num2)
    if operator == "+":
        answer = number1 + number2
    elif operator == "-":
        answer = number1 - number2
    elif operator == "*":
        answer = number1 * number2
    elif operator == "/":
        answer = number1 / number2
    return answer


num1, operator, num2 = find_question(equation_lst)
answer = answer_question(num1, operator, num2)
print("The answer is:", answer)