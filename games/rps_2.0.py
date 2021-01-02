from random import randint

does_P_want_to_play = True

C_WIN = "Killer KOMPUTER WINS !!!!"
P_WIN = "Perfect PLAYER WINS !!!!"

def does_P_want_to_play_again(continue_or_not):
    while continue_or_not == True:
                continue_or_not_checker = input("Would you like to continue: Yes or No?")                
                if continue_or_not_checker == "Yes":
                    print("One more time!")
                    break
                elif continue_or_not_checker == "No":
                    print("Maybe next time!")
                    continue_or_not=False
                else:
                    print("Check your spelling and try again!")
    return continue_or_not

def rock_paper_scissors_thingy(C,P,continue_or_not):
    while continue_or_not is True:
        comp = randint(1, 3)
        player = int(input("1)Rock" + "\n" + "2)Paper" + "\n" + "or" + "\n" + "3)Scissors" + "\n" + "?"))
        if player == 1 or player == 2 or player == 3:
            if player == comp:
                print("TIE!!!!")
            elif player == 1:
                if comp == 2:
                    print(C)
                elif comp == 3:
                    print(P)
            elif player == 2:
                if comp == 1:
                    print(P)
                elif comp == 3:
                    print(C)
            elif player == 3:
                if comp == 1:
                    print(C)
                elif comp == 2:
                    print(P)
            continue_or_not = does_P_want_to_play_again(continue_or_not)
            if continue_or_not == False:
                break
        else:
            print("Sorry! Incorrect Number! Try Again!")

rock_paper_scissors_thingy(C_WIN,P_WIN,does_P_want_to_play)