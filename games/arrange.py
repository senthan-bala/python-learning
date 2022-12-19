list_input = input("How many numbers do you want to put in the list?:")


number_list = []
number_list2 = []


for abc in range(int(list_input)):
    list_input2 = input("Choose a random number:")
    number_list.append(int(list_input2))


length = len(number_list) + len(number_list2)

for i in range(length):
    min_number = min(number_list)
    number_list2.append(min_number)
    number_list.remove(min_number)
    length = len(number_list) + len(number_list2)


print(number_list2)
