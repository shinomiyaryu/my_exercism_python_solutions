def value(colors):
    values = ''
    count = 0
    for color in colors:
        count += 1
        if count > 2:
            break
        if color == 'black':
            values += '0'
        elif color == 'brown':
            values += '1'
        elif color == 'red':
            values += '2'
        elif color == 'orange':
            values += '3'
        elif color == 'yellow':
            values += '4'
        elif color == 'green':
            values += '5'
        elif color == 'blue':
            values += '6'
        elif color == 'violet':
            values += '7'
        elif color == 'grey':
            values += '8'
        elif color == 'white':
            values += '9'
    return int(values)
    #pass
