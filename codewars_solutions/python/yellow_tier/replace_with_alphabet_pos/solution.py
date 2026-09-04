
ALPHABET = [chr(i) for i in range(97, 123)] # lower case letters

def alphabet_position(text):
    final_list = []

    for letter in text:
        letter = letter.lower()
        if letter not in ALPHABET:
            continue
        else:
            final_list.append(str(ALPHABET.index(letter) + 1))

    return " ".join(final_list)

print(alphabet_position("The sunset sets at twelve o' clock."))
