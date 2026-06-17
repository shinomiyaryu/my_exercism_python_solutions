def is_isogram(string):
    list_letters = []
    for letter in string:
        if letter.isalpha():
            if letter.lower() in list_letters:
                return False
            else:
                list_letters.append(letter.lower())
    return True
    #pass
