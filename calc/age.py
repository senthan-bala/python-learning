current_time = "12,18,2022"


def ask_for_birth(current_time):
    is_date_valid = False
    current_year = int(current_time[6:])
    current_month = int(current_time[:2])
    current_day = int(current_time[3:5])
    print(
        "This is the present day:", current_month, ",", current_day, ",", current_year
    )
    birth = input("When were you born?(Please type in numbers,ex; 2,27,1993):")
    month, day, year = birth.split(",")

    if year.isdigit() == False:
        print("Sorry thats not a valid date!")
        while not is_date_valid:
            birth = input("When were you born?(Please type in numbers,ex; 2,27,1993):")
            month, day, year = birth.split(",")
            if year.isdigit() == False:
                print("Sorry thats not a valid date!")
            if year.isdigit() == True:
                is_date_valid = True

    if int(month) <= current_month and int(day) <= current_day:
        years_old = current_year - int(year)
        months_old = current_month - int(month)
        days_old = current_day - int(day)
    elif int(month) > current_month and int(day) > current_day:
        years_old = current_year - int(year) - 1
        months_old = (current_month + 12) - int(month) - 1
        days_old = current_day - int(day) + 30
    elif int(month) > current_month and int(day) <= current_day:
        years_old = current_year - int(year) - 1
        months_old = (current_month + 12) - int(month)
        days_old = current_day - int(day)
    elif int(month) <= current_month and int(day) > current_day:
        years_old = current_year - int(year)
        months_old = current_month - int(month) - 1
        days_old = current_day - int(day) + 30

    print("Years old:", years_old, ", Months old:", months_old, ", Days old:", days_old)


ask_for_birth(current_time)
