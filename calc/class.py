people = [{'name':'senthan', 'age':10, 'gen':'boy'}, {'name':'megeraj', 'age':9, 'gen':'boy'}, {'name':'vardi', 'age':9, 'gen':'girl'}, {'name':'nila', 'age':4, 'gen':'girl'}]

for person in people:
    if person['age'] < 5:
        person['class'] = 'k'
    elif person['age'] > 5 and person['gen'] == 'boy':
        person['class'] = 'a'
    elif person['age'] > 5 and person['gen'] == 'girl':
        person['class'] = 'b'
    
    if person['gen'] == 'boy':
        person['money'] = person['age']*5
    elif person['gen'] == 'girl':
        person['money'] = person['age']*4

    print(person)

