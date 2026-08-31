def duplicate_encode(word):
    letters_list = []
    word = word.lower()

    for letter in word:
        if word.count(letter) > 1:
            letters_list.append(")")
        else:
            letters_list.append("(")
    
    return "".join(letters_list)
