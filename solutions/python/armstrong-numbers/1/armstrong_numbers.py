def is_armstrong_number(number):
    number_l = list(str(number))
    result = 0
    for digit in number_l:
        result += int(digit) ** len(number_l)
    if result == number:
        return True
    return False
    #pass
