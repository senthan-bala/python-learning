
operation = 'A'
a = 4
b = 15
c = 0

if operation == 'M':
    print('Multiplying')
    c = a * b
else:
    print('Adding')
    c = a + b

print(c)


if a >= 4:
    print('Big number')
else:
    print('Small number')

if a != 4:
    print('Not 4')
else:
    print('It is 4')

if a < 4 or a > 10:
    print('Too small or too big')
else:
    print('Perfect')


ate_breakfast = False
ate_lunch = False

if ate_breakfast or ate_lunch:
    print('You are ok')
else:
    print('You are starving and')

if ate_breakfast and ate_lunch:
    print('You are full')
else:
    print('You did not eat well')

food_ready = False

if food_ready:
    print('Food is ready')

a = 20
if a < 5:
    print('Baby age')
elif a > 100:
     print('Insane age')
elif a >= 20:
     print('Adult age')
else:
    print('Kid age')

age = 4

if age < 25:
    print('Some Student')
    if age < 5:
        print('Baby')
    elif age > 20:
        print('Going to college')
    else:
        if age <= 11:
            print('Elementary school')
        else:
            print('Middle or High school')
else:
    print('Too old to go to school')
