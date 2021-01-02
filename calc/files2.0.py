file_1 = open("games/files/friends.txt", "r")
txt = file_1.read()
lines = txt.splitlines()


def find_gen_age_name(lines: list):
    names = []
    list_1 = []
    for line in lines:
        dic = {}
        name, age, gender = line.split(",")
        dic["name"] = name
        dic["age"] = age
        dic["gender"] = gender
        if gender == "male" and int(age) < 15:
            list_1.append(dic)
            names.append(name)
    return list_1, names


def match_gen_age_name(list_1, names):
    for name in names:
        for dic in list_1:
            if dic["name"] == name:
                print(dic["name"],',', dic["age"],',', dic["gender"])


list_1, names = find_gen_age_name(lines)
names.sort()
match_gen_age_name(list_1, names)
