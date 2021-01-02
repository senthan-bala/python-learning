sentence = input("Type a sentence, I am going to change it: ")
words = sentence.split()
words_2 = []


def all_lower(words):
    w2 = []
    for word in words:
        word = word.lower()
        w2.append(word)
    return w2


words_2 = all_lower(words)

words_3 = []
for word in words_2:
    first_letter = word[0]
    first_letter = first_letter.upper()
    rest_letters = word[1:]
    word2 = first_letter + rest_letters
    words_3.append(word2)

sentence_2 = " "
sentence_2 = sentence_2.join(words_3)

print(sentence_2)

