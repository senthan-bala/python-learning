def read_file():
    file_1 = open("games/files/students.txt", "r")
    content = file_1.read()
    lines = content.splitlines()
    file_1.close()
    return lines


def find_or_create(name, students):
    for student in students:
        if name == student["name"]:
            return student

    new_student = {
        "name": name,
        "subjects": {"Math": {}, "English": {}, "Science": {}, "Music": {}},
    }
    students.append(new_student)
    return new_student


def make_students(lines):
    students = []
    for line in lines:
        name, subject, quarter, score = line.split(", ")
        student = find_or_create(name, students)
        student["subjects"][subject][quarter] = int(score)
    return students


lines = read_file()
students = make_students(lines)
print(students)
