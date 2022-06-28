from random import randint
go_again=True
while go_again ==True:
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
    qwerty=True
    while qwerty:
        want_to=input("Do you want to go again?")
        want_to.strip(" ")
        if want_to.isalpha()==True:
            qwerty=False
            want_to = want_to.lower()
            isyesno=False

            while isyesno==False:
                if want_to=="yes":
                    go_again=True
                    isyesno=True
                elif want_to=='no':
                    go_again=False
                    isyesno=True
                else:
                    isyesno=True
                    qwerty=True
                    print("please type yes or no")
        else:
            qwerty=True
            print("please type a word")
        
                



