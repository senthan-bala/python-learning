def read_file():
    file_1 = open("games/files/family.txt", "r")
    txt = file_1.read()
    lines = txt.splitlines()
    people = []
    for line in lines:
        person = build_person(line)
        people.append(person)
    return people


def build_person(line):
    person = {}
    name, age, gender = line.split(",")
    person["name"] = name
    person["age"] = age
    person["gender"] = gender
    return person


def list_ages(people):
    ages = []
    for person in people:
        age = person["age"]
        ages.append(int(age))
    return ages


def find_person_with_age(people, age):
    for person in people:
        if age == int(person["age"]):
            return person


def print_people(people, ages):
    for age in ages:
        person = find_person_with_age(people, age)
        print(person)


people = read_file()
ages = list_ages(people)
ages.sort(reverse=True)
print_people(people, ages)
