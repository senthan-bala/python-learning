characters = "abcdefghijklmnopqrstuvwxyz"
key = 12
message = input("Type a word: ")
encrypted_msg = ""
for a in message:
    if a in characters:
        find_pos = characters.find(a)
        new_pos = find_pos + key
        if new_pos >= 26:
            new_pos = new_pos - 26
        new_char = characters[new_pos]
        encrypted_msg += new_char
    else:
        encrypted_msg += a

print(encrypted_msg)
