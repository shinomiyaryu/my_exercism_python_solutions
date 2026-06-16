def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number > 0:
        aliquot_sum = 0
        for digit in range(1, number):
            if number % digit == 0:
                aliquot_sum += digit
        if aliquot_sum == number:
            return 'perfect'
        if aliquot_sum > number:
            return 'abundant'
        if aliquot_sum < number:
            return 'deficient'
    else:
        raise ValueError('Classification is only possible for positive integers.')
    #pass
