ages = [10, 3, 1, 2, 4, 6, 8, 5, 9, 7, 0]


def calc_age_group(age):
    if age <= 5 and age > 0:
        print("Debbie the baby")
    elif age > 5 and age <= 12:
        print("Kid")
    elif age >= 13 and age < 18:
        print("Teen")
    elif age >= 100:
        print("Too old")
    elif age >= 18:
        print("Adult")
    else:
        print("You are guybg    wwqwefifbqwguqe wqqwefgg  qr yunot alive")


def calc_schools(age):
    if age > 5 and age <= 25:
        print("Student")
        if age > 5 and age <= 11:
            print("Elementary")
        elif age <= 14 and age > 12:
            print("Middle")
        elif age <= 18 and age >= 15:
            print("High")
        elif age <= 25 and age >= 19:
            print("College")
    elif age > 25 and age < 60:
        print("Job")
    else:
        print("Baby or retired")


def full_calc(age):
    print("\nProcessing age:", age)
    calc_age_group(age)
    calc_schools(age)


for i in ages:
    full_calc(i)