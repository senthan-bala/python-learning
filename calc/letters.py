letters = input("Type a word, I am going to change it: ")


def reverse(word):
    length = len(word)
    rev_letters = ""

    for i in range(length - 1, -1, -1):
        rev_letters = rev_letters + word[i]
    return rev_letters


def uplow(word):
    rev_up_low = ""

    for letter in word:
        if letter.islower() == True:
            rev_up_low = rev_up_low + letter.upper()
        if letter.isupper() == True:
            rev_up_low = rev_up_low + letter.lower()
    return rev_up_low


letters = reverse(letters)
letters = uplow(letters)
print("New word:", letters)
