def square_of_sum(number):
    total = 0
    for i in range(1, number + 1):
        total += i
    return total**2
    #pass


def sum_of_squares(number):
    total = 0
    for i in range(1, number + 1):
        total += i**2
    return total
    #pass


def difference_of_squares(number):
    total = square_of_sum(number) - sum_of_squares(number)
    return total
    #pass
