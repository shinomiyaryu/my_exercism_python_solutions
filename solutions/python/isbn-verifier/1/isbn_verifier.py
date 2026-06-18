def is_valid(isbn):
    new_isbn = isbn.replace('-', '')
    if len(new_isbn) == 10 and new_isbn[:-1].isdigit():
        if new_isbn[-1].isalpha() and not new_isbn.endswith('X'):
            return False
        if new_isbn.endswith('X'):
            new_isbn = new_isbn[:-1] + '10'
        if (int(new_isbn[0]) * 10 + int(new_isbn[1]) * 9 + int(new_isbn[2]) * 8 + int(new_isbn[3]) * 7 + int(new_isbn[4]) * 6 + int(new_isbn[5]) * 5 + int(new_isbn[6]) * 4 + int(new_isbn[7]) * 3 + int(new_isbn[8]) * 2 + int(new_isbn[9:]) * 1) % 11 == 0:
            return True
    return False
    #pass