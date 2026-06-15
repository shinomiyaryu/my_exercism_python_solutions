def steps(number):
    step = 0
    target = number
    if target > 0:
        while target > 1:
            if target % 2 == 0:
                target /= 2
                step += 1
            if target % 2 != 0 and target != 1:
                target *= 3
                target += 1
                step += 1
        return step
    else:
        raise ValueError('Only positive integers are allowed')
    #pass
