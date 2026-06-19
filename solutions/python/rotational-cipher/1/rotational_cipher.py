def rotate(text, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ciphertext = ''
    if key <= 26:
        for letter in text:
            if letter.islower():
                index = alphabet.find(letter) + key
                if index > 25:
                    new_index = (key - (25 - alphabet.find(letter))) - 1
                    ciphertext += alphabet[new_index]
                else:
                    ciphertext += alphabet[index]
            if letter.isupper():
                index = ALPHABET.find(letter) + key
                if index > 25:
                    new_index = (key - (25 - ALPHABET.find(letter))) - 1
                    ciphertext += ALPHABET[new_index]
                else:
                    ciphertext += ALPHABET[index]
            if letter.isascii() and not letter.isalpha():
            #if letter.isdigit() or letter == ' ':
                ciphertext += letter
        return ciphertext
            
    #pass
