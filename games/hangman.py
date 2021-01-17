import random

words = [
    "workspace",
    "bookworm",
    "beekeeper",
    "microwave",
    "stronghold",
    "lightbulb",
    "transplant",
    "vaporize",
    "transcript",
    "walkway",
    "witchcraft",
    "glowworm",
    "bagpipes",
    "peekaboo",
]

hang_max = 6
max_empty_letters = 5

print("rfgbcuyer")


def pick_word(words):
    letter_indexes = []
    answers = []
    word = list(random.choice(words))
    word2 = word.copy()
    for i in range(max_empty_letters + 1):
        letter_index = random.randint(1, len(word2) - 1)
        letter_indexes.append(letter_index)
        if word2[letter_index] != "_":
            answers.append(word2[letter_index])
        word2[letter_index] = "_"
        if i == max_empty_letters:
            new_word = list(word2)
    cheat_sheet(answers, word)
    return new_word, answers, word, letter_indexes


def cheat_sheet(answers, word):
    for i in range(0, len(answers), -1):
        switch = answers[0]
        replacement = answers[i]
        replacement2 = replacement.copy()
        for i2 in range(0, len(word)):
            checker = word[i2 - 1]
            if checker == answers[i]:
                answers[i] = switch
                answers[0] = replacement2


def list_to_string(new_word):
    str_new_word = ""
    for letter in new_word:
        str_new_word += letter
    return str_new_word


def check_if_right(guess, answers, hang_man):
    is_guess_correct = False
    if len(guess) == 1:
        if guess.isalpha() == True:
            if guess in answers:
                print("Nice job!")
                answers.remove(guess)
                is_guess_correct = True
            else:
                hang_man = hang_man + 1
                if hang_man != hang_max:
                    print(
                        "Better luck next time! You have ",
                        hang_max - hang_man,
                        " tries left",
                    )
        else:
            print("Not a letter!")
    else:
        print("Not the right length!")
    return is_guess_correct, hang_man


def update_new_word(new_word, guess, word, letter_indexes):
    for i in letter_indexes:
        if guess == word[i]:
            new_word[i] = guess


def ask_for_answer(new_word, answers, word, letter_indexes):
    hang_man = 0
    is_word_done = False
    while not is_word_done:
        did_P_win = True
        str_word = list_to_string(word)
        str_new_word = list_to_string(new_word)
        print("Try to fill in this word: ", str_new_word)
        guess = input("Type here: ")
        guess = guess.strip()
        is_guess_correct, hang_man = check_if_right(guess, answers, hang_man)
        if is_guess_correct == True:
            update_new_word(new_word, guess, word, letter_indexes)

        for i in new_word:
            if i == "_":
                did_P_win = False

        if did_P_win == True:
            print("You won, yay!")
            is_word_done = True
        elif hang_man == hang_max:
            print("Sorry, you lose! Maybe next time!")
            print("The real word was: ", str_word)
            is_word_done = True


new_word, answers, word, letter_indexes = pick_word(words)
ask_for_answer(new_word, answers, word, letter_indexes)