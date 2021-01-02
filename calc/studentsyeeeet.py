def read_file():
    file_1 = open("games/files/students.txt", "r")
    content = file_1.read()
    lines = content.splitlines()
    file_1.close()
    return lines


def find_or_create_student(student_name: str, students: list):
    for student in students:
        if student_name == student["name"]:
            return student
    new_student = {
        "name": student_name,
        "subjects": {"Math": {}, "English": {}, "Science": {}, "Music": {}},
    }

    students.append(new_student)
    return new_student


def build_students(lines):
    students = []
    for line in lines:
        student_name, subject_name, quarter, score = line.split(",")
        student = find_or_create_student(student_name, students)
        student["subjects"][subject_name.strip()][quarter.strip()] = int(score.strip())
    return students


def check_student(students):
    name = input("Which student would you like to check?")
    is_student_real = False
    student_file = None
    for student in students:
        if name.strip().lower() == student["name"].strip().lower():
            is_student_real = True
            student_file = student
            break
    return is_student_real, student_file


def check_grade(students):
    check_for_more_students = True
    while check_for_more_students:
        is_student_real = False
        while not is_student_real:
            is_student_real, student_file = check_student(students)
            if is_student_real == True:
                print(student_file)
                break
            else:
                print("Sorry that is not a real student")
        keep_going = get_keep_going()
        if keep_going == "no":
            check_for_more_students = False


def get_keep_going():
    is_keep_going_valid = False
    while not is_keep_going_valid:
        keep_going = input("Do you want to keep going? Yes or No:")
        keep_going = keep_going.strip().lower()
        if keep_going == "no" or keep_going == "yes":
            is_keep_going_valid = True
            return keep_going
        else:
            print("That is not a valid input")

def add_student(students):
    is_student_val = False
    while not is_student_val:
        new_student_name = input("What is the name of the student?")
        new_student_name = new_student_name.strip().capitalize()        
        if not new_student_name.isalpha():
            print("Sorry that is not a valid name.")
            continue
        for student in students:
            if new_student_name == student['name']:
                print("Sorry that is not a valid name.")
                is_student_same = True
        if is_student_same == False:
            is_student_val = True
            return new_student_name

def add_student_main(students):
    is_student_adding_done = False
    while not is_student_adding_done:
        new_student_name=add_student(students)
        new_student = {
            "name": new_student_name,
            "subjects": {
                "Math": {"Q1": 0, "Q2": 0, "Q3": 0},
                "English": {"Q1": 0, "Q2": 0, "Q3": 0},
                "Science": {"Q1": 0, "Q2": 0, "Q3": 0},
                "Music": {"Q1": 0, "Q2": 0, "Q3": 0},
            },
        }
        print("Here is your new student file:", new_student)
        students.append(new_student)
        keep_going = get_keep_going()
        if keep_going == "no":
            break
    return students


def ask_action(students):
    are_actions_finished = False
    while not are_actions_finished:
        action = input("What action would you like to perform? Change, Check, or Add?")
        action = action.strip().lower()
        if action == "add":
            students = add_student_main(students)
        elif action == "change":
            print("change")
        elif action == "check":
            check_grade(students)
        elif action == "":
            break
        else:
            print("That is not a valid action! Try again!")


lines = read_file()
students = build_students(lines)
ask_action(students)
