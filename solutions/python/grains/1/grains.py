def square(number):
    grains = 2
    if number <= 0 or number > 64:
        raise ValueError("square must be between 1 and 64")
    elif number == 1:
        return 1
    elif number == 2:
        return 2

    for pos in range(3, 65):
        grains *= 2
        if pos == number:
            return grains
        
    #pass


def total():
    total = 3
    grains = 2
    for pos in range(3, 65):
        grains *= 2
        total += grains
    return total
    #pass
