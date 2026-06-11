"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    Parameters:
        number (int): Total number of seat letters to be generated.

    Returns:
        generator: A generator that yields seat letters.

    Note:
        Seat letters are generated from A to D.
        After D the sequence starts again with A.
        For example: A, B, C, D, A, B

    """
    counter = 0
    #seat_maker = []
    while counter < number:
        for seat in ['A','B','C','D']:
            #seat_maker.append(seat)
            yield seat
            counter += 1
            if counter == number:
                break
        
    '''for seat in seat_maker:
        yield seat'''
    #pass


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    Parameters:
        number (int): The total number of seats to be generated.

    Returns:
        generator: A generator that yields seat numbers.

    Note:
        A seat number consists of the row number and the seat letter.
        There is no row 13, and each row has 4 seats.

        Seats should be sorted from low to high.
        For example: 3C, 3D, 4A, 4B

    """
    #number_of_seats = []
    next_letter = generate_seat_letters(number)
    counter = 0
    row_number = 1
    seat_per_row = 0
    while counter < number:
        counter += 1
        if seat_per_row < 4:
            #number_of_seats.append(row_number)
            yield f'{row_number}{next(next_letter)}'
            seat_per_row += 1
        else:
            row_number += 1
            if row_number == 13:
                row_number += 1
            #number_of_seats.append(row_number)
            yield f'{row_number}{next(next_letter)}'
            seat_per_row = 1
    '''next_letter = generate_seat_letters(number)
    for seat in number_of_seats:
        yield f'{seat}{next(next_letter)}'
        '''
    #pass


def assign_seats(passengers):
    """Assign seats to passengers.

    Parameters:
        passengers (list[str]): A list of strings containing names of passengers.

    Returns:
        dict: With passenger names as keys and seat numbers as values.
        Example output: {"Adele": "1A", "Björk": "1B"}

    """
    passenger_seats = {}
    available_seats = generate_seats(len(passengers))
    for name in passengers:
        passenger_seats[name] = next(available_seats)
    return passenger_seats
    #pass


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    Parameters:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): A string containing the flight identifier.

    Returns:
        generator: A generator that yields 12 character long ticket codes.

    """
    for number in seat_numbers:
        char_length = len(number) + len(flight_id)
        padding = 12 - char_length
        zeros = '0' * padding
        yield f'{number}{flight_id}{zeros}'

    #pass
