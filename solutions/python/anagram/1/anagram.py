def find_anagrams(word, candidates):
    valid_anagrams = []
    lower_word = word.lower()
    for item in candidates:
        l_item = item.lower()
        if len(item) == len(word) and l_item != lower_word:
            match = 0
            for letter in l_item:
                if l_item.count(letter) == lower_word.count(letter):
                    match += 1
            if match == len(l_item):
                valid_anagrams.append(item)
    return valid_anagrams
    #pass
