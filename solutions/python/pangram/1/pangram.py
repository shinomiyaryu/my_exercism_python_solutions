def is_pangram(sentence):
    alphabet = []
    for letter in sentence:
        if letter.lower() not in alphabet and letter.isalpha():
            alphabet.append(letter)
    if len(alphabet) == 26:
        return True
    return False
    #pass
