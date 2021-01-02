from random import randint


computer = randint(1, 3)
print("1=r 2=p 3=s")
player = int(input("1, 2 or 3"))


print(player, "vs", computer)

if player == computer:
    print("DRAW!!!")
elif player == 1:
    if computer == 2:
        print("Computer wins!!!")
    else:
        print("Player wins!!!")
elif player == 2:
    if computer == 1:
        print("Player wins!!!")
    else:
        print("Computer wins!!!")
elif player == 3:
    if computer == 1:
        print("Computer wins!!!")
    else:
        print("Player wins!!!")
else:
    print("you didn't print a correct number")
