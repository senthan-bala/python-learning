numbers = [4356, 5679, 9876, 25454, 7676467]


def check_if_div(num):
    half_num = num / 2
    half_num2 = int(half_num)
    num2 = half_num2 * 2
    if num2 == num:
        even_or_odd = "even"
    elif num2 != num:
        even_or_odd = "odd"
    return even_or_odd


def print_if_div(lst):
    for item in lst:
        even_or_odd = check_if_div(item)
        if even_or_odd == "even":
            print(item, " = even ")
        elif even_or_odd == "odd":
            print(item, "= odd ")


print_if_div(numbers)
